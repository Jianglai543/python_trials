from j_多实例栈 import *


class StackLog(Stack2):
    pushs = 0
    pops = 0
    def __init__(self, start=[]):
        self.num = 0
        Stack2.__init__(self, start)

    def push(self, obj):
        Stack2.push(self, obj)
        StackLog.pushs += 1
        self.num = max(self.num, len(self))# len(self) 不懂啊

    def pop(self):
        x = Stack2.pop(self)
        StackLog.pops += 1
        return x

    def stats(self):
        return StackLog.pops, StackLog.pushs, self.num
