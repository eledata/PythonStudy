#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 2020/9/23 16:35 
@Author : Huang Moyue
@Mail : huangmoyue@163.com
@wechat : huangmoyue
"""
from celery_test.celery_task import send_email,send_message
# .delay是celery自带的参数
result = send_email.delay("yuan")
print(result.id)
print(result)
result2 = send_message.delay("alex")
print(result2.id)