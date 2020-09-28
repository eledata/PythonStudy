#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on 2020/8/12 9:09 
@Author : Huang Moyue
@Mail : huangmoyue@163.com
@wechat : huangmoyue
"""

# 7.1 可接受任意数量参数的函数
# def arg(arg, *args, **kwargs): -->> *args: tuple **kwargs: dict
def arg(arg, *args, **kwargs):
    print(arg)
    print(args)
    for key, value in kwargs.items():
        print(key)
        print(value)

arg(1,2,3,4,5, t = 11, m = 19)

# 7.2 你希望函数的某些参数强制使用关键字参数传递
def arg_use_name(arg, *, block):
    print(arg)
    print(block)
arg_use_name(arg = 10, block = 100)

# 7.3 给函数参数增加元信息，增加函数的可读性
def func_usage(a:int) -> int:
    print(a)
    return 10
# 7.7 匿名函数捕获变量值 你用lambda定义了一个匿名函数，并想在定义时捕获到某些变量的值
"""
这其中的奥妙在于lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的。 
因此，在调用这个lambda表达式的时候，x的值是执行时的值。例
"""
func_lambda_loop = [lambda x, n = n: x + n for n in range(5)]
for func in func_lambda_loop:
    print(func(10))



import math
from functools import partial
points = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)
pt = (4, 3)
tmp = partial(distance, pt)
for item in points:
    print(tmp(item))

points.sort(key=partial(distance,pt)) # list 根据key来排序

for item in points:
    print(tmp(item))

