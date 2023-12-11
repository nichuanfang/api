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
    curr_page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    try:
        return Result.success(movie_handler.get_movies(curr_page, page_size))
    except Exception as e:
        return Result.fail(e)


@blueprint.route('/update_movie_share_link', methods=['POST'])
def update_movie_share_link():
    """更新电影分享链接

    Returns:
        _type_: 更新结果
    """
    # 获取请求参数tmdb_id和share_link
    tmdb_id = request.form.get('tmdb_id')
    share_link = request.form.get('share_link')
    if not tmdb_id or not share_link:
        return Result.fail('tmdb_id和share_link不能为空')
    try:
        movie_handler.update_share_link(tmdb_id, share_link)
        return Result.success()
    except Exception as e:
        return Result.fail(e)
