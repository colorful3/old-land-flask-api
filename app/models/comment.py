# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, String, orm

from app.models.base import Base

__author__ = 'Colorful'
__date__ = '2018/8/19 上午4:56'


class Comment(Base):
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, comment='用户id')
    book_id = Column(Integer, comment='书籍id')
    nums = Column(Integer, comment='词条评论点赞数量')
    content = Column(String(255), comment='评论内容', nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['book_id', 'nums', 'content']
