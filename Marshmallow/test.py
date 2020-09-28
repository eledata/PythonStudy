#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 2020/9/23 14:23 
@Author : Huang Moyue
@Mail : huangmoyue@163.com
@wechat : huangmoyue
"""
import datetime as dt
from marshmallow import Schema, fields

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

from marshmallow import pprint
# dump --> dict
# dumps --> json
user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dumps(user) # 转化成str
print(type(result))
pprint(result)

org_result = schema.loads(result)
print(org_result)


user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users_list = [user1, user2]

# option 1:
schema_many = UserSchema(many=True)
result_list = schema_many.dump(users_list)
print(result_list)


"""
Marshmallow中的Validation功能用于校验客户端传入的数据是否规范，通常用于创建和修改数据。
Validation可分为 field level validation和 schema level validation，创建schema时，实现必要Validation是必须的，
由于详细阐述占用的篇幅会比较长，这部分内容请大家直接查看官方文档：
"""
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

data, errors = UserSchema().load({'age': 42}, partial=True)
# OR UserSchema(partial=True).load({'age': 42})
data, errors  # => ({'age': 42}, {})

