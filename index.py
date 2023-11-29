from flask import Flask
import requests
import os

app = Flask(__name__)


@app.route('/')
def home():
    # 获取环境变量github-token的值
    return os.environ.get('GH_TOKEN')


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