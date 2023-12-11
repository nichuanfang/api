from flask import Flask
from flask_cors import CORS
from core import bootstrap

# 创建一个flask 应用
app = Flask(__name__)
# 允许跨域
CORS(app)
# 挂载路由 启动项目
bootstrap.mount(app=app)

if __name__ == '__main__':
    bootstrap.run(app)
