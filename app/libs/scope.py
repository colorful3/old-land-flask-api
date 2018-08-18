# -*- coding: utf8 -*-
"""
权限配置文件
"""
__author__ = 'Colorful'
__date__ = '2018/8/17 下午11:32'


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        """优化点：1、实现链式相加 2、运算符重载。__add__ 3、去重"""
        self.allow_api = self.allow_api + other.allow_api
        self.allow_module = self.allow_module + other.allow_module
        self.forbidden = self.forbidden + other.forbidden
        self.allow_api = list(set(self.allow_api))
        self.allow_module = list(set(self.allow_module))
        self.forbidden = list(set(self.forbidden))
        return self


class AdminScope(Scope):
    def __init__(self):
        pass


class UserScope(Scope):
    allow_module = ['v1.like']
    allow_api = ['get_favor_info', 'get_my_favor']

    def __init__(self):
        pass


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    print_name = splits[0]
    view_func_name = splits[1]
    if view_func_name in scope.forbidden:
        return False
    if view_func_name in scope.allow_api:
        return True
    if print_name in scope.allow_module:
        return True
    else:
        return False
