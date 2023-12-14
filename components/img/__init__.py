# 图片接口
from flask import Blueprint, request
from core.result import Result
from components.img import img_handler

# 创建蓝图
blueprint = Blueprint('img', __name__, url_prefix='/img')


@blueprint.route('/<img_id>')
def get_img(img_id):
    """获取图片

    Args:
        img_id (str): 图片id

    Returns:
        _type_: 图片
    """
    try:
        return img_handler.get_img(img_id)
    except Exception as e:
        return Result.fail(e)
