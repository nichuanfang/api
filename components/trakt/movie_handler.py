# 电影处理类
from db.turso import acquire_client_sync
from core.result import Page
from core import cache

# 查询总数
TOTAL_COUNT = 'SELECT COUNT(*) FROM movie'
# 分页查询电影列表
QUERY_MOVIE_BY_PAGED = 'SELECT * FROM movie LIMIT :page_size OFFSET :offset'


@cache.cache_with_expiry(1)
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


def clear_cache():
    """清除缓存
    """
    # 过期时间 cache_expiry_time
    # 清空缓存
    get_movies.cache_clear()
