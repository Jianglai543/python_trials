"""class Class(object):
    x = 1
    def __init__(self, y):
        self.y = y

    def say(self):
        print(self.y)

    @classmethod
    def method(cls):
        print(cls)
        cls.x = 3
        cls(5).say()
        print(cls.x)



value = Class.x
Class.method()
print(value)"""

from decorator import decorate

def wrapper(func, *args, **kwargs):
    """print log before a function."""
    print( "[DEBUG] : enter {}()".format( func.__name__))
    return func(*args, **kwargs)

def logging(func):
    return decorate(func, wrapper)  # 用wrapper装饰func

def say(str):
    return str


if __name__ == '__main__':
    print(logging(say))