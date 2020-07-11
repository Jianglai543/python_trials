import time


def test(num, func, *args):
    start = time.clock()
    for _ in range(num):
        func(*args)
    return time.clock() - start

