#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 2020/9/23 16:22 
@Author : Huang Moyue
@Mail : huangmoyue@163.com
@wechat : huangmoyue
"""
import celery
import time

# 任务结果储存，使用redis的1号仓库
backend = 'redis://861117@127.0.0.1:6379/1'
# 消息中间件，使用redis的2号仓库
broker = 'redis://861117@127.0.0.1:6379/2'

# 创建celery对象
cel = celery.Celery('task', backend=backend, broker=broker)


@cel.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return "ok"

@cel.task
def send_message(name):
    print("向%s发送短信..." % name)
    time.sleep(5)
    print("向%s发送短信完成" % name)
    return "ok"