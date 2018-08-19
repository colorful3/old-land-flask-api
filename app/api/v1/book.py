# -*- coding: utf8 -*-

from flask import jsonify, g

from app.libs.c_blueprints import CBlueprint
from app.libs.error_code import Success
from app.libs.token_auth import auth
from app.models.book import Book
from app.models.keywords import Keywords
from app.models.like import Like
from app.spider.douban_book import DouBanBook
from app.validaters.forms import\
    BookSearchForm, BookDetailForm, CommentAdd, BookForm
from app.view_models.book import BookCollection

__author__ = 'Colorful'
__date__ = '2018/8/13 上午1:19'


api = CBlueprint('book')


@api.route('/hot_list', methods=['GET'])
def get_hot():
    res = Book.get_hot(summary=1)
    return jsonify(res)


@api.route('/<int:book_id>/short_comment', methods=['GET'])
def get_short_comment(book_id):
    form = BookForm(data={'book_id': book_id}).validate_for_api()
    res = Book.get_comments(form.book_id.data)
    return jsonify(res)


@api.route('/favor/count', methods=['GET'])
@auth.login_required
def get_favor_num():
    uid = g.user.uid
    filters = {
        Like.uid == uid,
        Like.status == 1,
        Like.book_id != ""
    }
    count = Like.query.filter(*filters).count()
    return jsonify({"count": count})


@api.route('/<int:book_id>/favor', methods=['GET'])
@auth.login_required
def favor_status(book_id):
    form = BookForm(data={'book_id': book_id}).validate_for_api()
    favor = Book.get_favor_status(form.book_id.data)
    return jsonify(favor)


@api.route('/add/short_comment', methods=['POST'])
@auth.login_required
def add_comment():
    form = CommentAdd().validate_for_api()
    Book.add_comment(form.book_id.data, form.content.data)
    return Success()


@api.route('/hot_keyword', methods=['GET'])
def get_hot_keyword():
    """TODO 使用redis管理热词"""
    res = Keywords.query.filter_by().order_by(
        Keywords.nums.desc()).limit(15).all()
    result = [k_o.keyword for k_o in res]
    return jsonify({"hot": result})


@api.route('/search', methods=['GET'])
def search():
    form = BookSearchForm().validate_for_api()
    books = BookCollection()

    douban_book = DouBanBook()
    q = form.q.data.strip()
    douban_book.search(q, form.start.data, form.count.data)

    books.fill(
        douban_book, form.start.data,
        form.count.data, form.summary.data)

    return jsonify(books)


@api.route('/<int:id>/detail', methods=['GET'])
def detail(id):
    form = BookDetailForm({'id': id}).validate_for_api()
    books = BookCollection()

    douban_book = DouBanBook()
    douban_book.get_by_id(book_id=form.id.data)

    books.fill(douban_book)
    return jsonify(books.first)
