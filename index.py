from http import client
from flask import Flask
from flask import request
import json
from db import turso
import os
# from utils import github
# import requests

# turso获取客户端(同步)
client = turso.acquire_client_sync()
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


@app.route('/api', methods=['GET'])
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text


@app.route('/turso', methods=['GET'])
def turso_query():
    """turso查询

    Parameters:
        sql: sql语句
    """
    client = turso.acquire_client_sync()
    result = client.execute('SELECT * FROM frameworks')
    # 转为str
    res = []
    for row in result:
        res.append(row['url'])
    return res
