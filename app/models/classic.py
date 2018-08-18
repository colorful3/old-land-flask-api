# -*- coding: utf8 -*-
from flask import g
from sqlalchemy import Column, Integer, Text, String, SmallInteger, ForeignKey, select, and_
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.image import Image
from app.models.like import Like

__author__ = 'Colorful'
__date__ = '2018/8/14 上午12:06'


class Classic(Base):
    """
    期刊模型
    type 类型号 100 200 300 分别表示电影，音乐，句子
    TODO 把image从Classic表中拆分，新增模型image
    """
    id = Column(Integer, primary_key=True, comment='期刊在数据中序号，供点赞使用')
    content = Column(Text, default='', comment='期刊内容')
    image = relationship(Image)
    img_id = Column(Integer, ForeignKey('image.id'))
    index = Column(SmallInteger, comment='期号')
    title = Column(String(100), default='', comment='期刊题目')
    author = Column(String(100), default='', comment='作者')
    type = Column(SmallInteger, default=100, comment='期刊类型,这里的类型分为:100 电影 200 音乐 300 句子')
    url = Column(String(100), default='', nullable=True, comment='当type为300时，此字段为音乐url')

    def keys(self):
        return ['content', 'id', 'image_url', 'fav_nums', 'like_status',
                'index', 'create_datetime', 'title', 'author', 'type', 'url']

    @property
    def latest(self):
        res = Classic.query.filter_by().order_by(Classic.id.desc()).first_or_404()
        return res

    @property
    def image_url(self):
        return self.image.image

    @property
    def fav_nums(self):
        count = Like.query.filter_by(cid=self.id).count()
        return count

    @staticmethod
    def next(index):
        next_item = index + 1
        res = Classic.query.filter_by(index=next_item).first_or_404()
        return res

    @staticmethod
    def previous(index):
        previous_item = index - 1
        return Classic.query.filter_by(index=previous_item).first_or_404()

    @staticmethod
    def detail(type, id):
        return Classic.query.filter_by(type=type, id=id).first_or_404()

    @staticmethod
    def favor_info(type, id):
        uid = g.user.uid
        res = Like.query.filter_by(cid=id, uid=uid, type=type).count()
        fav_nums = Like.query.filter_by(cid=id, type=type).count()
        result = dict(
            fav_nums=fav_nums,
            id=id,
            like_status=1 if res else 0
        )
        return result

    @staticmethod
    def my_favor(start=1, count=20):
        uid = g.user.uid
        filters = {
            Like.uid == uid,
            Like.cid > 0,
            Like.status == 1
        }
        like_list = Like.query.filter(*filters).paginate(int(start), int(count), False)
        items = like_list.items
        res = [Classic.query.filter_by(id=item.cid).first() for item in items]
        return res


    @property
    def like_status(self):
        # TODO 感觉老师的小程序获取点赞这里有bug（不排除是故意这么设计的），当你的期刊已经点赞，别人再打开小程序取消点赞，居然自己的小程序中点赞也取消了？？？
        if 'user' in g:
            uid = g.user.uid
        else:
            uid = 0
        if not uid:
            status = 0
        else:
            status = 1 if Like.query.filter_by(cid=self.id, uid=uid).first() else 0
        return status
