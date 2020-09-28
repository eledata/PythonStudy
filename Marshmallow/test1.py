#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 2020/9/23 15:11 
@Author : Huang Moyue
@Mail : huangmoyue@163.com
@wechat : huangmoyue
"""
from marshmallow import Schema, fields, ValidationError

def validate_quantity(n):
    if n < 0:
        raise ValidationError('Quantity must be greater than 0.')
    if n > 30:
        raise ValidationError('Quantity must not be greater than 30.')

class ItemSchema(Schema):
    quantity = fields.Integer(validate=validate_quantity)

in_data = {'quantity': 31}
err = None

result, errors = ItemSchema().load(in_data)

