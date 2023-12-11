# 项目启动
from flask import Flask
from flask_cors import CORS
from components import blueprints
# 导出所有components下__init__.py的蓝图文件


def init(app: Flask, host: str = '127.0.0.1', port: int = 5555, debug: bool = False):

    # 挂载蓝图
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # 允许跨域
    CORS(app)
    # 项目启动
    app.run(host=host, port=port, debug=debug)
