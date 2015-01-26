# -*- coding:utf-8 -*-
__author__ = 'kiven'

'''实现python range函数'''

def my_range(start, stop=None, step=None):
    result = []
    s = 1  # 步长
    if not step is None:
        s = step
    if not stop is None:
        while True:
            if start < stop:
                result.append(start)
                start += s
            else:
                break
    else:
        stop,start = start,0
        while True:
            if start < stop:
                result.append(start)
                start += s
            else:
                break
    return result

print my_range(1,10,4)
print range(1,10,4)