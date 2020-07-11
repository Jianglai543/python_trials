class Stack():

    def __init__(self, start=None):
        if start is None:
            start = []
        self.stack = None
        for i in range(-len(start), 0):
            self.push(start[-i-1])

    def push(self, obj):
        self.stack = obj , self.stack

    def pop(self):
        node, self.stack = self.stack
        return node

    def __len__(self):
        len, tree = 0, self.stack
        while tree:
            len += 1
            tree = tree[1]
        return len

    def __getitem__(self, item):
        index = 0
        while self.stack and index < item:
            index += 1
            self.stack = self.stack[1]
        if self.stack:
            return self.stack[0]
        else:
            raise IndexError()

    def __repr__(self):
        return '[FastStack:' + repr(self.stack) + "]"
