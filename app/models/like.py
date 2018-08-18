# -*- coding: utf8 -*-
from sqlalchemy import Integer, Column, String, SmallInteger

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/18 上午11:27'


class Like(Base):
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, default=0, comment='用户id')
    cid = Column(Integer, default=0, comment='期刊id')
    isbn = Column(String(15), nullable=True)
    type = Column(SmallInteger, default=100, comment='合理利用数据冗余，期刊类型')

