#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 14:45
# @Author  : 南风有时起
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

bp = Blueprint('api', __name__)

# 写在最后是为了防止循环导入，ping.py文件也会导入 bp
from app.api import ping, tokens, errors, users, posts, comments