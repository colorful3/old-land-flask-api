# -*- coding: utf8 -*-
from app.libs.error import APIException

__author__ = 'Colorful'
__date__ = '2018/8/14 上午10:33'


class Success(APIException):
    """返回成功相关信息"""
    code = 201
    error_code = 0
    msg = 'OK'


class ServerError(APIException):
    """为调用的时候提高可读性"""
    def __init__(self):
        super(ServerError, self).__init__()


class ClassicMissException(APIException):
    """期刊没找到异常"""
    code = 404
    error_code = 3000
    msg = 'classic not found'


class ParameterException(APIException):
    """参数异常"""
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
