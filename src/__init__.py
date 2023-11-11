from flask import Flask
from src.models.ConnectDB import ConnectDB

app = Flask(__name__)

app.config['SECRET_KEY'] = '290665ddf7d91ef58dc2f6c500a15eb0'

db = ConnectDB()

from src import routes