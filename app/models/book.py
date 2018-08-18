# -*- coding: utf8 -*-
import json

from flask import jsonify, g
from sqlalchemy import Column, Integer, String, Float, Text, orm

from app.libs.error_code import Forbidden, NotFound
from app.models.base import Base, db
from app.models.comment import Comment
from app.models.like import Like

__author__ = 'Colorful'
__date__ = '2018/8/19 上午2:54'


class Book(Base):
    id = Column(Integer, primary_key=True)
    _author = Column('author', String(255), comment='作者，多个作者序列化')
    category = Column(String(100), comment='分类')
    image = Column(String(100), comment='书籍图片')
    isbn = Column(String(50), comment='书籍isbn')
    pages = Column(Integer, comment='书籍页数')
    price = Column(Float, comment='书籍价格')
    pubdate = Column(String(20), comment='发布时间')
    publisher = Column(String(50), comment='出版社')
    subtitle = Column(String(50), comment='主题标题')
    summary = Column(Text, comment='描述')
    title = Column(String(100), comment='书名')
    _translator = Column('translator', String(255), comment='译者')
    fav_nums = Column(Integer, default=0, comment='收藏数')

    @orm.reconstructor
    def __init__(self):
        self.fields = [
            'id', 'author', 'category',
            'image', 'isbn', 'pages', 'price',
            'pubdate','publisher', 'subtitle',
            'summary', 'title', 'translator',
            'fav_nums', 'like_status'
        ]

    @property
    def author(self):
        return json.loads(self._author)

    @property
    def translator(self):
        return json.loads(self._translator)

    @property
    def like_status(self):
        return 0

    @staticmethod
    def get_hot(summary):
        """得到热门书籍（概要）"""
        result = Book.query.filter_by().order_by(
            Book.fav_nums.desc(), Book.id.desc()
        ).limit(20).all()
        if summary:
            result = [book.hide(
                'category', 'isbn', 'pages',
                'price', 'pubdate', 'publisher',
                'subtitle', 'summary', 'translator'
            ) for book in result]
        return result

    @staticmethod
    def add_comment(book_id, content):
        uid = g.user.uid
        count = Comment.query.filter_by(uid=uid, book_id=book_id).count()
        if count:
            raise Forbidden(msg='You already commented on')
        with db.auto_commit():
            comment = Comment()
            comment.uid = uid
            comment.book_id = book_id
            comment.content = content
            comment.nums = 1
            db.session.add(comment)

    @staticmethod
    def get_comments(book_id):
        comments = Comment.query.filter_by(book_id=book_id).all()
        if not comments:
            raise NotFound(msg='no comment')
        c = [comment for comment in comments]
        res = {
            "comment": c,
            "book_id": book_id
        }
        return res

    @staticmethod
    def get_favor_status(book_id):
        uid = g.user.uid
        res = Like.query.filter_by(book_id=book_id, uid=uid).count()
        fav_nums = Like.query.filter_by(book_id=book_id).count()
        result = dict(
            fav_nums=fav_nums,
            id=book_id,
            like_status=1 if res else 0
        )
        return result
