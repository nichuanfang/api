from flask import Flask
import requests
import os

app = Flask(__name__)


@app.route('/')
def home():
    # 获取环境变量github-token的值
    try:
        token = os.environ['GH_TOKEN']
        if token == '':
            return '环境变量为空'
    except:
        return '环境变量无法获取'
    return token


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text