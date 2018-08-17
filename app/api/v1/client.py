# -*- coding: utf8 -*-
from app.libs.c_blueprints import CBlueprint
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.models.user import User
from app.validaters.forms import ClientForm

__author__ = 'Colorful'
__date__ = '2018/8/17 下午6:05'


api = CBlueprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    """暂时不需要此接口"""
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: __register_by_user_email,
        ClientTypeEnum.USER_MINA: __register_by_mina  # 微信小程序不需要注册，所以该方法暂时保留
    }
    promise[form.type.data]()

    return Success()


def __register_by_user_email():
    pass


def __register_by_mina():
    User()
    pass
