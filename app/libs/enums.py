# -*- coding: utf8 -*-
from enum import Enum

__author__ = 'Colorful'
__date__ = '2018/8/14 上午1:22'


class ClassicEnums(Enum):
    """期刊枚举类"""
    CLASSIC_MOVIE = 100
    CLASSIC_MUSIC = 200
    CLASSIC_SENTENCE = 300
    BOOK = 400


class ClientTypeEnum(Enum):
    """客户端类型枚举类"""
    USER_EMAIL = 100
    USER_MOBILE = 101
    USER_MINA = 200  # 微信小程序
    USER_WX = 201  # 微信公众号
