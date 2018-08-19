# -*- coding: utf8 -*-
from flask import g
from sqlalchemy import Integer, Column, SmallInteger, orm

from app.libs.enums import ClassicEnums
from app.libs.error_code import Forbidden
from app.models.base import Base, db

__author__ = 'Colorful'
__date__ = '2018/8/18 上午11:27'


class Like(Base):
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, default=0, comment='用户id')
    cid = Column(Integer, default=0, comment='期刊id')
    book_id = Column(Integer, default=0, comment='书籍id')
    type = Column(SmallInteger, default=100, comment='合理利用数据冗余，期刊类型')

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'id', 'uid', 'cid', 'book_id', 'type'
        ]

    @staticmethod
    def add_favor(art_id, type):
        uid = g.user.uid
        if type == ClassicEnums.BOOK.value:
            count = Like.query.filter_by(uid=uid, type=type, book_id=art_id).count()
        else:
            count = Like.query.filter_by(uid=uid, type=type, cid=art_id).count()
        if count > 0:
            raise Forbidden(msg='You had already collection', error_code=2000)
        with db.auto_commit():
            like = Like()
            like.uid = uid
            if type == ClassicEnums.BOOK.value:
                like.book_id = art_id
            else:
                like.cid = art_id
            like.type = type
            db.session.add(like)

    @staticmethod
    def cancel(art_id, type):
        uid = g.user.uid
        with db.auto_commit():
            if type == ClassicEnums.BOOK:
                Like.query.filter_by(uid=uid, type=type, book_id=art_id).delete()
            else:
                Like.query.filter_by(uid=uid, type=type, cid=art_id).delete()
