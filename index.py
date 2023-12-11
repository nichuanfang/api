from flask import Flask
from flask_cors import CORS
from core import bootstrap

if __name__ == '__main__':
    # 创建一个flask 应用
    app = Flask(__name__)
    # 允许跨域
    CORS(app)
    # 挂载路由 启动项目
    bootstrap.init(app=app)
