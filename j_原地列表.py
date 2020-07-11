class error(Exception):  pass


class Stack3():

    def __init__(self, start=[]):
        self.stack = []
        for i in start:   self.push(i)

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:   raise error('cannot pop')
        return self.stack.pop()

    def top(self):
        if not self.stack:   raise error('cannot get top value')
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, item):
        return self.stack[item]

    def __repr__(self):
        return '[Stack :%s]' % self.stack