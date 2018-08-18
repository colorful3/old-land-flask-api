# -*- coding: utf8 -*-
"""
自定义API异常类，对HTTPException的get_body和get_headers方法的重写
"""
from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = 'Colorful'
__date__ = '2018/8/14 上午10:21'


class APIException(HTTPException):
    code = 500
    msg = 'Life can\'t always be colorful ￣□￣｜｜'
    error_code = 1006

    def __init__(self, code=None, msg=None, error_code=None, headers=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__(description=msg, response=None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_path()
        )
        return json.dumps(body)

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_path():
        full_path = request.full_path
        main_path = full_path.split('?')
        return main_path[0]
