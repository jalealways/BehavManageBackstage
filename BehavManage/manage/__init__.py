#  coding=utf-8

from flask import Flask
from config import *
from flask_cors import *

app = Flask(__name__, static_folder=static_folder, static_url_path='')
CORS(app, supports_credentials=True)

from api import test
from api import behavManage