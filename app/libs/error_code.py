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


class WXException(APIException):
    """微信内部异常"""
    code = 500
    msg = "WeChat exception, It's not our problem"
    error_code = 5000


class AuthFailed(APIException):
    """token授权异常"""
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    """禁止访问"""
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004


class NotFound(APIException):
    """资源没有找到"""
    code = 404
    msg = 'sorry, the resource was not found on the server'
    error_code = 1002
