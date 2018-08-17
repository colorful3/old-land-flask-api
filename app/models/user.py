# -*- coding: utf8 -*-
import requests
from flask import current_app
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.libs.c_http import HTTP
from app.libs.error_code import WXException
from app.models.base import Base, db

__author__ = 'Colorful'
__date__ = '2018/8/17 下午5:55'


class User(Base):
    """
    用户模型
    """
    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), nullable=True)
    open_id = Column(String(50), nullable=True, unique=True)
    email = Column(String(50), nullable=True)
    auth = Column(SmallInteger, default=1, comment='用户权限级别（1：user 2：管理员）')
    _password = Column('password', String(100))
    avatar = Column(String(100), nullable=True, comment='用户头像')
    extend = Column(String(255), nullable=True, comment='扩展字段')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def get_openid(code):
        """获取openid"""
        mina_appid = current_app.config['MINA_APPID']
        mina_se = current_app.config['MINA_SECRET']
        mina_login_url = current_app.config['MINA_LOGIN_URL'].format(mina_appid, mina_se, code)

        wx_result = HTTP.get(mina_login_url)
        login_failed = 'errcode' in wx_result.keys()
        if login_failed:
            # TODO 写入日志
            raise WXException(msg=wx_result['errmsg'], error_code=wx_result['errcode'])
        if wx_result is None:
            raise WXException()
        return wx_result

    @staticmethod
    def register_by_mina():
        pass

    @staticmethod
    def verify():
        pass

    @staticmethod
    def mina_verify(code):
        user = User()
        wx_result = user.get_openid(code)
        openid = wx_result['openid']
        user_info = User.query.filter_by(open_id=openid).first()
        if user_info is None:
            with db.auto_commit():
                user.open_id = openid
                db.session.add(user)
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}
