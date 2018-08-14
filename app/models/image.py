# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/14 上午12:48'


class Image(Base):
    id = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False, comment='地址')
    form_type = Column(SmallInteger, default=1, comment='1 来自本地，2 来自公网')
