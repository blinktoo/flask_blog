#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 23:01
# @Author  : 南风有时起
# @File    : __init__.py
# @Software: PyCharm
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/blog?charset=utf8"