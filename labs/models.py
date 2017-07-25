# coding: utf-8
from __future__ import unicode_literals
from mongoengine import *


class Name(EmbeddedDocument):
    last_name = StringField()
    first_name = StringField()


# 为了防止notExit错误，要使用动态文档类型
class PpInfor(DynamicDocument):
    # 注意类型
    zkymp = StringField()  # 中科院杂志分区
    DOI = StringField()  # DOI
    category = StringField()  # 类别
    accessNum = StringField()  # 入藏号
    quoted = StringField()  # 他引
    publish = StringField()  # 发表
    index = IntField()  # 序号
    fiyf = StringField()  # 5y IF
    foreign = StringField()  # 是否是国外，是‘1’，否‘0’或空
    native = StringField()  # 是否是国内，是‘1’，否‘0’或空
    SCI = StringField()  # 是否SCI，是‘1’，否‘0’或空
    JCR = StringField()  # JCR分区-2015，是‘1’，否‘0’或空
    rank = IntField()  # 排名
    notes = StringField()  # 备注
    EI = StringField()  # 是否EI，是‘1’，否‘0’或空
    pub_time = IntField()  # 发布时间，年份 !!!!注意类型
    URL = StringField()  # 论文链接
    quote = StringField()  # 引用
    title = StringField(unique=True)  # 论文名称
    pub_name = StringField()  # 发表刊物名称
    autor_name = ListField(EmbeddedDocumentField(Name))  # 作者姓名
    commu_name = StringField()  # 是否为通信作者，是‘1’，否‘0’或空
    tzofif = StringField()  # 2015IF
    tzozif = StringField()  # 2010IF

    # 创建索引,论文名称和发表时间
    meta = {
        'indexes': [
            'title',  # $title
            'pub_time',
        ],
        'collection': 'ppInfor'
    }


class User(Document):
    num = StringField()
    name = StringField()
    pwd = StringField()
    email = StringField()

    meta = {
        'collection': 'user'
    }
