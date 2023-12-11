# 项目启动
from flask import Flask
from components import blueprints
# 导出所有components下__init__.py的蓝图文件


def mount(app: Flask):
    # 挂载蓝图
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def run(app: Flask, debug: bool = False):
    """本地启动项目

    Args:
        app (Flask): _description_
        debug (bool, optional): _description_. Defaults to False.
    """
    app.run(debug=debug)
