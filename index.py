from http import client
from flask import Flask
from flask import request
import json
from db import turso
import os

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
