from flask import Blueprint, request
from core.result import Result
from components.trakt import movie_handler, show_handler

# 创建蓝图
blueprint = Blueprint('spotify', __name__, url_prefix='/spotify')


@blueprint.route('/auth')
def auth():
    """spotify授权获取授权码

    Returns:
        _type_: _description_
    """
    return "success"
