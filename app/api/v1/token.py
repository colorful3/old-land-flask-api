# -*- coding: utf8 -*-
from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.libs.c_blueprints import CBlueprint
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validaters.forms import UserMinaForm

__author__ = 'Colorful'
__date__ = '2018/8/17 下午6:45'


api = CBlueprint('token')


@api.route('/mina', methods=['POST'])
def get_mina_token():
    """获取小程序的token"""
    form = UserMinaForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_MINA: User.mina_verify,
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    mina_code = form.code.data
    identify = promise[ClientTypeEnum(form.type.data)](mina_code)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(
        identify['uid'], form.type.data,
        identify['scope'], expiration
    )
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
