# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/13 9:03
import inspect


def a():
    print(inspect.stack()[0].function)
    print('a')

def b():
    a()

def test_stack():
    b()

