# -*- coding: utf8 -*-
from flask import jsonify

from app.libs.c_blueprints import CBlueprint
from app.libs.token_auth import auth
from app.models.classic import Classic
from app.validaters.forms import ClassicForm, ClassicDetailForm, ClassicFavorForm
from app.view_models.classic import ClassicCollection

__author__ = 'Colorful'
__date__ = '2018/8/13 上午12:45'

api = CBlueprint('classic')


@api.route('/latest', methods=['GET'])
def get_latest():
    res = Classic().latest
    classic = ClassicCollection()
    data = classic.fill_single(res)
    return jsonify(data)


@api.route('/<int:index>/next', methods=['GET'])
def get_next(index):
    form = ClassicForm(data={'index': index}).validate_for_api()
    res = Classic.next(form.index.data)
    classic = ClassicCollection()
    data = classic.fill_single(res)
    return jsonify(data)


@api.route('/<int:index>/previous', methods=['GET'])
def get_previous(index):
    form = ClassicForm(data={'index': index}).validate_for_api()
    res = Classic.previous(form.index.data)
    classic = ClassicCollection()
    data = classic.fill_single(res)
    return jsonify(data)


@api.route('/<int:type>/<int:id>', methods=['GET'])
def get_detail(type, id):
    form = ClassicDetailForm(data={'type': type, 'id': id}).validate_for_api()
    res = Classic.detail(form.type.data, form.id.data)
    classic = ClassicCollection()
    data = classic.fill_single(res)
    return jsonify(data)


@api.route('/<int:type>/<int:id>/favor', methods=['GET'])
@auth.login_required
def get_favor_info(type, id):
    form = ClassicFavorForm(data={'type': type, 'id': id}).validate_for_api()
    res = Classic.favor_info(form.type.data, form.id.data)
    return jsonify(res)


@api.route('/favor', methods=['GET'])
@auth.login_required
def get_my_favor():
    res = Classic.my_favor()
    classic = ClassicCollection()
    result = classic.fill(res)
    return jsonify(result)
