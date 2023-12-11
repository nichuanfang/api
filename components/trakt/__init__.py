import json
from flask import Blueprint
from db.turso import acquire_client_sync, libsql_client

# 创建蓝图
blueprint = Blueprint('blueprint', __name__, url_prefix='/trakt')


@blueprint.route('/movie')
def movies():
    """分页获取电影列表

    Returns:
        _type_: 电影列表
    """
    with acquire_client_sync() as turso_client:
        result = []
        # 执行查询
        result_set = turso_client.execute('SELECT * FROM movie')
        columns = result_set.columns
        for row in result_set.rows:
            data = {}
            for index in range(0, len(columns)):
                # 将查询结果转换为字典
                data[columns[index]] = row[index]
            result.append(data)

        return result
