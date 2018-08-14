# -*- coding: utf8 -*-
from sqlalchemy import Column, Integer, Text, String, SmallInteger, ForeignKey, desc
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.image import Image

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
    fav_nums = Column(Integer, default=0, comment='点赞次数')
    image = relationship(Image)
    img_id = Column(Integer, ForeignKey('image.id'))
    index = Column(SmallInteger, comment='期号')
    like_status = Column(SmallInteger, default=0, comment='是否点赞')
    title = Column(String(100), default='', comment='期刊题目')
    author = Column(String(100), default='', comment='作者')
    type = Column(SmallInteger, default=100, comment='期刊类型,这里的类型分为:100 电影 200 音乐 300 句子')
    url = Column(String(100), default='', nullable=True, comment='当type为300时，此字段为音乐url')

    @property
    def latest(self):
        return Classic.query.filter_by().order_by(desc(Classic.id)).all()
