"""diction1 = [{'name': 'qq', 'value': '20', 'weight': '20', 'per_weight': 1}, {'name': 'ww', 'value': '20', 'weight': '4', 'per_weight': 5}]
for item in diction1:print(f"get {item['name']}")
for item2 in diction1 : value = item2['per_weight']

print(value)"""
"""快速排序算法
def partition(arr, low, hight):
    i = low - 1
    for j in range(low, hight):
        if arr[j] <= arr[hight]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hight] = arr[hight], arr[i + 1]
    return i

def quick_sort(l, low, hight):
    if low < hight:
        key_Index = partition(l, low, hight)
        quick_sort(l, low, key_Index)
        quick_sort(l, key_Index + 1, hight)
    else:
        return

l = [5,8,1,3,15,12,0]
quick_sort(l, 0, len(l) - 1)
print("after sort:", l)"""

import time

def demo(func):
    def wrapped(*args):
        func(*args)
        time.sleep(2)
        time2 = time.time()
        print(time2)
    return wrapped


@demo
def f(a,b,c,d):
    start = time.time()
    time.sleep(1)
    end = time.time() + a + b + c + d
    print(end-start)

def demo_call(func):
    def wrapped():

        print(f'{func.__name__}')
        return func()
    return wrapped

@demo_call
def say_hello():
    print('hi')


def tag(tag_name):
    def add_content(content):
        print(f'{tag_name}, {content}')
    return add_content


def tag_it(name1):
    def wrapper1(func):
        def wrapper2(*args):
            content = func(*args)  # 函数是func
            return content, name1
        return wrapper2
    return wrapper1


@tag_it('bb')
def hello_sth(str1='world'):
    return f'hello {str1}'


def logging(level):
    def out_wrapper(func):
        def inner_wrapper(*args):
            func(*args)
            return func.__name__, level
        return inner_wrapper
    return out_wrapper


@logging(level='info')
def do(stri):
    print(f'do {stri}')


class Class_deo(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        value = self.func(*args) + 'hhh'
        return value

@Class_deo
def class_do(strrr):
    return strrr


class Class_logging(object):
    def __init__(self, strr='info'):
        self.strr = strr
    def __call__(self, func):
        def wrapper(*args):
            value3 = func(*args) + self.strr
            return value3
        return wrapper

@Class_logging('good')
def class_get_args(stringg):
    return stringg

from decorator import *

def wrapper(func, *args):
    print( func.__name__)
    return func(*args)

def logging(func):
    return decorate(func, wrapper)



if __name__ == '__main__':
    #   f(3,4,5,6)
    say_hello()
    tag_it = tag('aaa')
    tag_it(content='bbb')
    value = hello_sth('jianglai')
    print(value)
    print(do('homework'))  # 闭包和装饰器传参
    print(class_do('jianglai')) # 无法传参
    print(class_get_args('jianglai'))  # 无法传参
    print(logging(say_hello))





