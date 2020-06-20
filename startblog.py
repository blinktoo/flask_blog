#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 15:02
# @Author  : 南风有时起
# @File    : startblog.py
# @Software: PyCharm
from app import create_app, db
from app.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}