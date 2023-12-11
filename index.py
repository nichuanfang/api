from flask import Flask
from core import bootstrap

if __name__ == '__main__':
    # 创建一个flask应用
    app = Flask(__name__)
    # 挂载路由 启动项目
    bootstrap.init(app=app)
