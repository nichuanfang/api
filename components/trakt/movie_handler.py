# 电影处理类
from db.turso import acquire_client_sync
from core.result import Page
from core import cache

# 查询总数
TOTAL_COUNT = 'SELECT COUNT(*) FROM movie'
# 分页查询电影列表(按照最后观看时间排序)
QUERY_MOVIE_BY_PAGED = 'SELECT * FROM movie  ORDER BY last_watched_at DESC LIMIT :page_size OFFSET :offset'
# 更新分享链接
UPDATE_MOVIE_SHARE_LINK = 'UPDATE movie SET share_link = :share_link WHERE movie_id = :movie_id'
#  根据类型查询索引表数据
SELECT_LOCAL_SEARCH_BY_TYPE = "SELECT * FROM local_search WHERE type = ?"
# 根据movie_id查询电影详情
SELECT_MOVIE_BY_ID = "SELECT * FROM movie WHERE movie_id = ?"


@cache.cache_with_expiry(876000)
def get_movies(curr_page: int = 1, page_size: int = 10):
    """分页查询电影列表

    Args:
        curr_page (int, optional): 第几页. 默认1

        page_size (int, optional): 每页多少条数据. 默认10

    Returns:
        _type_: 电影列表
    """
    with acquire_client_sync() as turso_client:
        page = Page(curr_page, page_size)

        # 查询总数
        total_count: int = turso_client.execute(
            TOTAL_COUNT).rows[0][0]  # type: ignore
        # 设置总页数与总数
        page.set_total_count(total_count)
        if total_count == 0:
            return page

        page_data = []
        # 执行查询
        result_set = turso_client.execute(QUERY_MOVIE_BY_PAGED, {
            'page_size': page_size, 'offset': (curr_page - 1) * page_size})
        columns = result_set.columns
        for row in result_set.rows:
            data = {}
            for index in range(0, len(columns)):
                # 将查询结果转换为字典
                data[columns[index]] = row[index]
            page_data.append(data)
        page.data = page_data
        return page


@cache.cache_with_expiry(876000)
def get_movie(movie_id: str):
    """获取电影详情

    Args:
        movie_id (str): 电影的tmdb_id

    Returns:
        _type_: 电影详情
    """
    with acquire_client_sync() as turso_client:
        # 查询电影详情
        rows = turso_client.execute(
            SELECT_MOVIE_BY_ID, [movie_id]).rows
        if len(rows) == 0:
            return None
        return rows[0]


def update_share_link(movie_id: str, share_link: str):
    """更新分享链接

    Args:
        movie_id (int): 电影的tmdb_id
        share_link (str): 分享链接
    """
    with acquire_client_sync() as turso_client:
        turso_client.execute(UPDATE_MOVIE_SHARE_LINK, {
            'movie_id': movie_id, 'share_link': share_link})
        # 清除缓存
        get_movies.cache_clear()
        get_movie.cache_clear()


@cache.cache_with_expiry(876000)
def get_index():
    """获取电影索引

    Returns:
        _type_: 索引数据(base64编码)
    """
    with acquire_client_sync() as turso_client:
        # 查询电影索引
        rows = turso_client.execute(
            SELECT_LOCAL_SEARCH_BY_TYPE, ('movie',)).rows
        if len(rows) == 0:
            return ''
        return rows[0]['b64_index']
