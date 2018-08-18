# -*- coding: utf8 -*-
from flask import current_app
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/14 上午12:48'


class Image(Base):
    id = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False, comment='地址')
    from_type = Column(SmallInteger, default=1, comment='1 来自本地，2 来自公网')

    @property
    def image(self):
        if self.from_type == 1:
            url = current_app.config['BASIC_API_URL'] + self.url
        else:
            url = self.url
        return url
