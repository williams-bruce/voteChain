from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '290665ddf7d91ef58dc2f6c500a15eb0'

from src import routes