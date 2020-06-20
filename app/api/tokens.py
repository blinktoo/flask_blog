#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:36
# @Author  : 南风有时起
# @File    : tokens.py
# @Software: PyCharm
from flask import jsonify, g
from app import db
from app.api import bp
from app.api.auth import basic_auth, token_auth


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    '''
    注意上面的装饰器，第一次进网站就会来验证身份，
    当通过验证之后才能生成后续的token
    '''
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token': token})

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    g.current_user.revoke_token()
    db.session.commit()
    return '', 204