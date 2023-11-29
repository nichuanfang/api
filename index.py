from flask import Flask
from flask import request
from utils import github
import json
# import requests
# import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api',methods=['GET'])
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
    
# 增删改查demo
@app.route('/api_add')
def api_add():
    # 触发github workflow
    github.trigger_github_workflow('api_add', {'name': 'Jhon', 'age': 30})
    # 读取json文件
    with open('data.json', mode='r',encoding='utf-8') as my_file:
        text = my_file.read()
        # json转dict
        data = json.loads(text)
        # 增加数据
        data.append({'name': 'Jhon', 'age': 30})
        # dict转json
        text = json.dumps(data)
        github.trigger_github_workflow('api_add', {'name': 'Jhon', 'age': 30})
        return text