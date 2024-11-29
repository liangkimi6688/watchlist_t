# coding:utf-8
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = 'liang'
# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
# MySQL配置
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/watchlist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    user = User.query.get(int(user_id))
    return user

from . import views, errors, commands

# login_manager.login_message = 'Your custom message'


@app.context_processor
def inject_user():
    from .models import User
    user = User.query.first()
    return dict(user=user)

if __name__ == '__main__':
    app.run()
