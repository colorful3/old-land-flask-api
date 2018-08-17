# -*- coding: utf8 -*-
"""
    custom Blueprint
"""
__author__ = 'Colorful'
__date__ = '2018/8/13 上午1:34'


class CBlueprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        url_prefix = '/' + self.name if url_prefix is None else None
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
