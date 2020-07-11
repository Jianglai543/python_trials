class error(Exception):  pass


class Stack2:

    def __init__(self, start=None):
        if start is None:
            start = []
        self.stack = []
        for i in start:
            self.push(i)
        self.reverse()

    def push(self, obj):
        self.stack = [obj] + self.stack

    def pop(self):
        if not self.stack:
            raise error('cannot pop')
        obj, *self.stack = self.stack
        return obj

    def top(self):
        if not self.stack:
            raise error("cannot get top")
        return self.stack[0]

    def empty(self):
        return not self.stack

    def __repr__(self):
        return "<Stack:%s>" % self.stack

    def __eq__(self, other):
        return other.stack == self.stack

    def __len__(self):
        return len(self.stack)

    def __add__(self, other):
        return Stack2(self.stack + other.stack)

    def __mul__(self, reps):
        return Stack2(self.stack * reps)

    def __getitem__(self, item):
        return self.stack[item]

    def __getattr__(self, name):
        return getattr(self.stack, name)