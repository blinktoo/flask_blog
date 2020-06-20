#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 17:28
# @Author  : 南风有时起
# @File    : models.py
# @Software: PyCharm
import base64
from datetime import datetime, timedelta
import os

from flask import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class PaginatedAPIMixin(object):
    '''
    query: 查询对象
    page: 从第page页开始
    per_page: 每一页几个项
    endpoint: 用于构建指定的URL
    '''
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data

class User(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))  # 不保存原始密码
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            '_links': {
                'self': url_for('api.get_user', id=self.id)
            }
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):
        # 注意Now和utcnow的区别  一个获取电脑时间，一个获取标准时区的时间与电脑配置时间没有关系
        now = datetime.utcnow()
        # 如果有token 而且token没有过期就直接返回token
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        # 根据随机字符(os.urandom(24))做编码(b6encode)加密，在做解码 这就来作为token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        # 计算过期时间
        self.token_expiration = now + timedelta(seconds=expires_in)
        # 这个网上抄来的写法，感觉很秒阿，直接不用声明实例，真的妙！
        db.session.add(self)
        return self.token

    def revoke_token(self):
        # 减少过期时间
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        # 获取用户的时候先检查token是否过期
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user