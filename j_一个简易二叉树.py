class BinaryTree():
    def __init__(self):
        self.tree = EmptyNode()

    def __repr__(self):
        return repr(self.tree)

    def insert(self, value):
        self.tree = self.tree.insert(value)

    def lookup(self, value):
        return self.tree.lookup(value)


class EmptyNode():

    def __repr__(self):
        return '*'
    def insert(self, value):
        return BinaryNode(self, value, self)
    def lookup(self, value):
        return False


class BinaryNode():
    def __init__(self, left, value, right):
        self.left, self.value, self.right = left, value, right

    def __repr__(self):
        return ('(%s %s %s) ' % (repr(self.left), repr(self.value), repr(self.right)))

    def lookup(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            return self.left.lookup(value)
        else:
            return self.right.lookup(value)

    def insert(self, value):
        if value < self.value:
            self.left = self.left.insert(value)
        else:
            self.right = self.right.insert(value)
        return self


if __name__ == '__main__':
    x = BinaryTree()
    for i in [1,2,8,5,6] :
        x.insert(i)
        print(x)
    for i in range(8):
        print(i,  x.lookup(i))