# -*- coding: utf8 -*-
from flask import request

from app.libs.c_blueprints import CBlueprint

__author__ = 'Colorful'
__date__ = '2018/8/13 上午1:19'


api = CBlueprint('book')


@api.route('/hot_list', methods=['GET'])
def get_hot():
    return 'This is hot list'


@api.route('/<int:book_id>/short_comment')
def get_short_comment(book_id):
    return 'this is book short comment'
