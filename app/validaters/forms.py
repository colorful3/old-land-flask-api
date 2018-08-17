# -*- coding: utf8 -*-
from wtforms import StringField
from wtforms.validators import DataRequired, Email, length, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validaters.base import BaseForm as Form
__author__ = 'Colorful'
__date__ = '2018/8/13 下午3:45'


class TestForm(Form):
    """测试用"""
    test = StringField(validators=[
        DataRequired(message='test字段必须填写'),
        length(min=2, max=10)
    ])
    email = StringField(validators=[
        Email(message='invalidate email')
    ])


class ClientForm(Form):
    ac = StringField(validators=[
    ])
    se = StringField(validators=[
    ])
    type = StringField(validators=[
        DataRequired(message='type不能为空'),
    ])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserMinaForm(ClientForm):
    """小程序客户端校验类，客户端端通过code来换取openid"""
    code = StringField(validators=[
        DataRequired(message='sorry, code is required!')
    ])
