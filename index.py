from flask import Flask
from flask import request
# from utils import github
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
    