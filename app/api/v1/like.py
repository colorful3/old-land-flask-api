# -*- coding: utf8 -*-
from app.libs.c_blueprints import CBlueprint
from app.libs.error_code import Success
from app.libs.token_auth import auth

__author__ = 'Colorful'
__date__ = '2018/8/17 下午11:14'


api = CBlueprint('like')


@api.route('', methods=['POST'])
@auth.login_required
def add_like():
    return Success()


@api.route('/cancel', methods=['POST'])
def cancel_like():
    return Success()
    pass