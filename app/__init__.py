#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:42
# @Author  : 南风有时起
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册blueprint
    from app.api import bp as api_dp
    app.register_blueprint(api_dp, url_prefix='/api')

    return app