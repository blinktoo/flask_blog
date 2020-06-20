#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:42
# @Author  : 南风有时起
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Flask-SQLAlchemy 插件
db = SQLAlchemy()
# Flask-Migrate 插件
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 允许跨域 CORS
    CORS(app)
    # 装载 Flask-SQLAlchemy
    db.init_app(app)
    # 装载 Flask-Migrate
    migrate.init_app(app, db)

    # 注册blueprint
    from app.api import bp as api_dp
    app.register_blueprint(api_dp, url_prefix='/api')

    return app

from app import models