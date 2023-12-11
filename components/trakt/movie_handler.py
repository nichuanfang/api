# 电影处理类
from db.turso import acquire_client_sync

QUERY_MOVIE_BY_PAGED = 'SELECT * FROM movie LIMIT :page_size OFFSET :offset'


def get_movies(page: int = 1, page_size: int = 10):
    """分页查询电影列表

    Args:
        page (int, optional): 第几页. 默认1

        page_size (int, optional): 每页多少条数据. 默认10

    Returns:
        _type_: 电影列表
    """
    with acquire_client_sync() as turso_client:
        result = []
        # 执行查询
        result_set = turso_client.execute(QUERY_MOVIE_BY_PAGED, {
            'page_size': page_size, 'offset': (page - 1) * page_size})
        columns = result_set.columns
        for row in result_set.rows:
            data = {}
            for index in range(0, len(columns)):
                # 将查询结果转换为字典
                data[columns[index]] = row[index]
            result.append(data)
        return result
