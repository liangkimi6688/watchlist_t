# coding:utf-8
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

# 数据库配置
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/watchlist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库和迁移
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 初始化登录管理
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))

from watchlist import views, errors, commands

@app.context_processor
def inject_user():
    from .models import User
    user = User.query.first()
    return dict(user=user)

if __name__ == '__main__':
    app.run()