import heapq


class PriorityQueue(object):
    """完成优先级队列的类"""
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))    # 压栈，按格式，负优先级最小
        print(self._queue)
        self._index += 1

    def pop(self):
        print()
        return heapq.heappop(self._queue)[-1]  # item出栈


if __name__ == '__main__':
    q = PriorityQueue()
    q.push('a', 5)
    q.push('b', 4)
    q.push('c', 9)
    print(q.pop())
    print(q.pop())