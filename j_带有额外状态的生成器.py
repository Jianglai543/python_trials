from collections import deque


class filehistory:
    def __init__(self, lines, max_hist=3):
        self.lines = lines
        self.history = deque(maxlen=max_hist)

    def __iter__(self):
        for index, line in enumerate(itertools.dropwhile(lambda line : line.startswith('a'), self.lines)):  # 删除a开头行
            self.history.append((index, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    import itertools
    with open('j_yield.txt') as f:
        lines = filehistory(f)
        # lines2 = itertools.dropwhile(lambda line : line.startswith('a'), f)
        for line in lines:
            if 'python' in line:
                for i, line in lines.history:
                    print(i, line)

