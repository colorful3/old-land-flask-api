# -*- coding: utf8 -*-
from wtforms import StringField
from wtforms.validators import DataRequired, Email, length

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
