#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 15:04
# @Author  : 南风有时起
# @File    : ping.py
# @Software: PyCharm
from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('Pong!')