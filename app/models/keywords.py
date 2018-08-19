# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, orm

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/19 上午9:39'


class Keywords(Base):
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), comment='搜索关键字')
    nums = Column(Integer, comment='搜索次数')

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'keyword', 'nums']
