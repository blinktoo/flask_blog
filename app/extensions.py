#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 14:33
# @Author  : 南风有时起
# @File    : extensions.py
# @Software: PyCharm
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


# Flask-Cors plugin
cors = CORS()
# Flask-SQLAlchemy plugin
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# Flask-SQLAlchemy plugin
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
# # Flask-Migrate plugin
migrate = Migrate(render_as_batch=True)