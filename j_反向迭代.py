class countDown:
    """定义计数的迭代类"""
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        while self.start > 0:
            yield self.start  # 配合for 迭代
            self.start -= 1

    def __reversed__(self):
        n  = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    a = countDown(3)
    for i in a:
        print(i)
    a2 = countDown(3)
    for i in reversed(a2):
        print(i)
    from itertools import islice

    a3 = countDown(10)
    for i in islice(a3, 4, 9):  # 从第四个到第九个
        print(i)








