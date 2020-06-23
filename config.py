#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:45
# @Author  : 南风有时起
# @File    : config.py.py
# @Software: PyCharm
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/blog?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    POSTS_PER_PAGE = 10
    USERS_PER_PAGE = 10