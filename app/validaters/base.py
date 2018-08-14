# -*- coding: utf8 -*-
"""
重写wtforms的Form类，抛出自定义格式的参数异常
"""
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'Colorful'
__date__ = '2018/8/14 上午10:44'


class BaseForm(Form):
    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        """返回格式"""
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
