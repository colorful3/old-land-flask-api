# -*- coding: utf8 -*-
from app.view_models.base import BaseViewModel

__author__ = 'Colorful'
__date__ = '2018/8/19 上午12:52'


class BookViewModel(BaseViewModel):
    def __init__(self, book, is_summary=0):
        self.title = book['title']
        self.author = book['author']
        self.category = book['category'] if 'category' in book else ''
        self.id = book['id']
        self.image = book['image']
        self.images = book['images']
        self.isbn = book['isbn'] if 'isbn' in book else book['isbn13']
        self.pages = book['pages'] or ''
        self.price = book['price']
        self.pubdate = book['pubdate']
        self.publisher = book['publisher']
        self.subtitle = book['subtitle'] or ''
        self.summary = book['summary'] or ''
        self.translator = book['translator'] or ''
        self.is_summary = is_summary

    def keys(self):
        if int(self.is_summary) == 0:
            key_list = [
                'title', 'author', 'category', 'id',
                'image', 'isbn', 'pages', 'price',
                'pubdate', 'publisher', 'subtitle',
                'summary', 'translator'
            ]
        else:
            key_list = [
                'author', 'id', 'image',
                'isbn', 'price', 'title'
            ]
        return key_list


class BookCollection(BaseViewModel):
    def __init__(self):
        self.total = 0
        self.books = []
        self.start = 0
        self.count = 0

    def fill(self, book_data, start=1, count=20, summary=0):
        """
        格式化书籍列表的数据
        :param book_data: 未格式化数据
        :param start: 开始记录数，默认为0
        :param count: 记录条数，默认为20,超过依然按照20条计算
        :param summary: 返回完整或简介,默认为0,0为完整内容,1为简介
        :return:
        """
        self.books = [BookViewModel(book, is_summary=summary) for book in book_data.books]
        self.total = book_data.total
        self.start = start - 1
        self.count = count

    def keys(self):
        return ['total', 'books', 'start', 'count']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
