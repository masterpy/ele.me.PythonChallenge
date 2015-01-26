# -*- coding:utf-8 -*-
__author__ = 'kiven'

'''实现python xrange函数'''
# 跟range函数的实现没有大的变化,只是使用yield 表示生成器
def my_xrange(start, stop=None, step=None):
    result = []
    s = 1  # 步长
    if not step is None:
        s = step
    if not stop is None:
        while True:
            if start < stop:
                yield start
                start += s
            else:
                break
    else:
        stop,start = start,0
        while True:
            if start < stop:
                yield start
                start += s
            else:
                break