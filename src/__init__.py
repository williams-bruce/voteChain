from flask import Flask
from flask_session import Session
from src.models.ConnectDB import ConnectDB

app = Flask(__name__)

app.config['SECRET_KEY'] = '290665ddf7d91ef58dc2f6c500a15eb0'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = ConnectDB()

from src import routes