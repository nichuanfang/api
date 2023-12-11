# 项目启动
from flask import Flask
from components import blueprints
# 导出所有components下__init__.py的蓝图文件


def init(app: Flask, debug: bool = False):

    # 挂载蓝图
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # 项目启动
    app.run(debug=debug)
