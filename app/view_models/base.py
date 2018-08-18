# -*- coding: utf8 -*-
__author__ = 'Colorful'
__date__ = '2018/8/18 下午7:16'


class BaseViewModel:

    def keys(self):
        return []

    def __getitem__(self, item):
        return getattr(self, item)

