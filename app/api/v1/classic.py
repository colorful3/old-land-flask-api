# -*- coding: utf8 -*-
import json

from flask import request

from app.libs.c_blueprints import CBlueprint
from app.libs.error_code import ClassicMissException, Success
from app.models.classic import Classic
from app.validaters.forms import TestForm

__author__ = 'Colorful'
__date__ = '2018/8/13 上午12:45'

api = CBlueprint('classic')


@api.route('/latest', methods=['GET', 'POST'])
def get_latest():
    form = TestForm().validate_for_api()
    classic = Classic()
    data = form.data
    res = 1
    if not res:
        raise ClassicMissException()
    return Success()


@api.route('/<int:index>/next', methods=['GET'])
def get_next(index):
    return 'After the index of ' + str(index)


@api.route('/<int:index>/previous', methods=['GET'])
def get_previous(index):
    return 'Before the index of' + str(index)


@api.route('/<int:type>/<int:id>', methods=['GET'])
def get_detail(type, id):
    return 'type' + str(type) + ' id' + str(id) + ' detail'


"""
TODO 下面两个要做用户登录验证
"""


@api.route('/<int:type>/<int:id>/favor', methods=['GET'])
def get_favor_info(type, id):
    pass


@api.route('/favor', methods=['GET'])
def get_favor(type, id):
    pass
