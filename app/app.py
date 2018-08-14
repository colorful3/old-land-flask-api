# -*- coding: utf8 -*-
from flask import Flask

__author__ = 'Colorful'
__date__ = '2018/8/13 上午12:41'


def register_blueprints(app):
    """
    注册蓝图
    :param app: flask核心对象
    """
    from app.api import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    # 注册sqlalchemy
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    return app
