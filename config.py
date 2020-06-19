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
    pass