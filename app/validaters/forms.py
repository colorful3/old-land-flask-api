# -*- coding: utf8 -*-
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, length, ValidationError

from app.libs.enums import ClientTypeEnum, ClassicEnums
from app.libs.error_code import NotFound
from app.models.book import Book
from app.models.classic import Classic
from app.validaters.base import BaseForm as Form

__author__ = 'Colorful'
__date__ = '2018/8/13 下午3:45'


class TestForm(Form):
    """测试用"""
    test = StringField(validators=[
        DataRequired(message='test字段必须填写'),
        length(min=2, max=10)
    ])
    email = StringField(validators=[
        Email(message='invalidate email')
    ])


class ClientForm(Form):
    ac = StringField(validators=[
    ])
    se = StringField(validators=[
    ])
    type = IntegerField(validators=[
        DataRequired(message='type不能为空'),
    ])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserMinaForm(ClientForm):
    """小程序客户端校验类，客户端端通过code来换取openid"""
    code = StringField(validators=[
        DataRequired(message='sorry, code is required!')
    ])


class ClassicForm(Form):
    index = IntegerField(validators=[
        DataRequired()
    ])

    def validate_index(self, field):
        if isinstance(field.data, int) and field.data > 0:
            return True
        else:
            raise ValidationError('index must be positive integer')


class ClassicDetailForm(Form):
    id = IntegerField(validators=[
        DataRequired()
    ])
    type = IntegerField(validators=[
        DataRequired()
    ])

    def validate_id(self, field):
        if isinstance(field.data, int) and field.data > 0:
            return True
        else:
            raise ValidationError('id must be positive integer')

    def validate_type(self, value):
        try:
            ClassicEnums(value.data)
        except ValueError as e:
            raise e


class ClassicFavorForm(ClassicDetailForm):
    def validate_id(self, field):
        super(ClassicFavorForm, self).validate_id(field)
        count = Classic.query.filter_by(id=field.data).count()
        if count < 1:
            raise NotFound(msg='such a classic was not found')


class BookForm(Form):
    book_id = IntegerField(validators=[
        DataRequired()
    ])

    def validate_book_id(self, field):
        count = Book.query.filter_by(id=field.data).count()
        if count < 1:
            raise NotFound(msg='数据库中没有找到该书籍')
        return True


class BookSearchForm(Form):
    start = IntegerField(default=1)
    count = IntegerField(default=20)
    summary = IntegerField(default=0)
    q = StringField(validators=[
        DataRequired(message='请输入要检索的内容'),
        length(1, 50)
    ])


class BookDetailForm(Form):
    id = IntegerField(validators=[
        DataRequired()
    ])


class CommentAdd(BookForm):

    content = StringField(validators=[
        DataRequired(message='评论内容不能为空'),
        length(1, 12)
    ])


class LikeForm(Form):
    art_id = IntegerField(validators=[
        DataRequired()
    ])
    type = IntegerField(validators=[
        DataRequired
    ])

    def validate_type(self, value):
        try:
            ClassicEnums(value.data)
        except ValueError as e:
            raise e
