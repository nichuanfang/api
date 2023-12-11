from flask import Blueprint, request
from core.result import Result
from components.trakt import movie_handler, show_handler

# 创建蓝图
blueprint = Blueprint('blueprint', __name__, url_prefix='/trakt')


@blueprint.route('/movie')
def movies():
    """分页获取电影列表

    Returns:
        _type_: 电影列表
    """
    # 获取请求参数page和page_size
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    return Result.success(movie_handler.get_movies(page, page_size))
