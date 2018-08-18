# -*- coding: utf8 -*-
from app.libs.c_blueprints import CBlueprint
from app.libs.error_code import Success
from app.libs.token_auth import auth
from app.models.like import Like
from app.validaters.forms import LikeForm

__author__ = 'Colorful'
__date__ = '2018/8/17 下午11:14'


api = CBlueprint('like')


@api.route('', methods=['POST'])
@auth.login_required
def add_like():
    form = LikeForm().validate_for_api()
    Like.add(form.art_id.data, form.type.data)
    return Success()


@api.route('/cancel', methods=['POST'])
def cancel_like():
    form = LikeForm().validate_for_api()
    Like.cancel(form.art_id.data, form.type.data)
    return Success()
