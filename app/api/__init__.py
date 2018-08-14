# -*- coding: utf8 -*-
from flask import Blueprint

from app.api.v1 import classic, book

__author__ = 'Colorful'
__date__ = '2018/8/13 上午12:40'


def create_blueprint_v1():
    """
    创建v1 api的蓝图
    :return:
    """
    bp_v1 = Blueprint('v1', __name__)

    classic.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1


def create_blueprint_v2():
    """
    创建v2 api的蓝图
    :return:
    """
    pass
