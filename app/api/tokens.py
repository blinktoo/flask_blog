#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:36
# @Author  : 南风有时起
# @File    : tokens.py
# @Software: PyCharm
from flask import jsonify, g
from app.api import bp
from app.api.auth import basic_auth
from app.extensions import db


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    '''
    注意上面的装饰器，第一次进网站就会来验证身份，
    当通过验证之后才能生成后续的token
    '''
    # 调用get_jwt（）方法 ，把用户的几乎所有信息都包含到token中
    token = g.current_user.get_jwt()
    # 每次用户登录（即成功获取 JWT 后），更新 last_seen 时间 ping 来自于Post下的方法
    g.current_user.ping()
    db.session.commit()
    return jsonify({'token': token})
    # jwt 没办法回收(不需要delete)只能等它过期，所以有效时间别设置太长