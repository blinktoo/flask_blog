#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:13
# @Author  : 南风有时起
# @File    : auth.py
# @Software: PyCharm
from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.api.errors import error_response
from app.models import User

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    '''
    用于检查用户提供的用户名和密码
    g: 对象 和session有点像，不过session跨request g不跨个人感觉有点想前端的this
    '''
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)

@token_auth.verify_token
def verify_token(token):
    '''用于检查用户请求是否有token，并且token真实存在，还在有效期内'''
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None

@basic_auth.error_handler
def basic_auth_error():
    '''用于在认证失败的情况下返回错误响应'''
    return error_response(401)