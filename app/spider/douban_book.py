# -*- coding: utf8 -*-
import json

from app.libs.c_http import HTTP
from app.libs.error_code import NotFound
from app.models.base import db
from app.models.book import Book

__author__ = 'Colorful'
__date__ = '2018/8/19 上午12:32'


class DouBanBook:
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    bookid_url = 'https://api.douban.com/v2/book/{}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search(self, keyword, page=1, count=20):
        count = 20 if count > 20 else count
        url = self.keyword_url.format(keyword, count, self.calculate_start(page, count))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def get_by_id(self, book_id):
        url = self.bookid_url.format(book_id)
        result = HTTP.get(url)
        if not result:
            raise NotFound(msg='book not found')
        self.__fill_single(result)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']
            self.dataPersistence()

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def dataPersistence(self):
        """持久化数据"""
        for single in self.books:
            if not Book.query.filter_by(isbn=single['isbn']).count():
                with db.auto_commit():
                    book = Book()
                    book.author = json.dumps(single['author'])
                    book.category = single['category']
                    book.image = single['image']
                    book.isbn = single['isbn']
                    book.pages = single['pages']
                    book.price = single['price']
                    book.pubdate = single['pubdate']
                    book.publisher = single['publisher']
                    book.subtitle = single['subtitle']
                    book.summary = single['summary']
                    book.title = single['title']
                    book.translator = json.dumps(single['translator'])
                    db.session.add(book)

    @staticmethod
    def calculate_start(page, count):
        return (page - 1) * count


if __name__ == '__main__':
    book = DouBanBook()
    book.search('C')
    pass
