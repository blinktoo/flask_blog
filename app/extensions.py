#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 14:33
# @Author  : 南风有时起
# @File    : extensions.py
# @Software: PyCharm
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Flask-Cors plugin
cors = CORS()
# Flask-SQLAlchemy plugin
db = SQLAlchemy()
# # Flask-Migrate plugin
migrate = Migrate()