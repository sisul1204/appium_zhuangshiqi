# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/12 9:04
from functools import wraps


def f(a):
    def extend(func):
        @wraps(func)
        def hello(*args, **kwargs):
            print(a)
            print('hello')
            print(args)
            print(kwargs)
            func(*args, **kwargs)
            print('good bye')
        return hello
    return extend

@f('lizhipeng')
def tmp(a, b, c=1):
    print('tmp')


def test_wrapper():
    tmp(1, 2, c=7)

