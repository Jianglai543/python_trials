class KeyBinaryTree():
    def __init__(self):
        self.tree = EmptyNode()

    def __repr__(self):
        return repr(self.tree)

    def insert(self, key, value):
        self.tree = self.tree.insert(key, value)

    def lookup(self, key):
        return self.tree.lookup(key)


class EmptyNode():

    def __repr__(self):
        return 'None'
    def insert(self, key, value):
        return BinaryNode(self, key, value, self)
    def lookup(self, value):
        return False


class BinaryNode():
    def __init__(self, left, key, value, right):
        self.left, self.key, self.value, self.right = left, key, value, right

    def __repr__(self):
        return ('(%s %s:%s %s) ' % (repr(self.left), repr(self.key), repr(self.value), repr(self.right)))

    def lookup(self, key):
        if key == self.key:
            return self.value
        elif key < self.key:
            return self.left.lookup(key)
        else:
            return self.right.lookup(key)

    def insert(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:
            self.left = self.left.insert(key, value)
        else:
            self.right = self.right.insert(key, value)
        return self

if __name__ == '__main__':
    a = KeyBinaryTree()
    for (key, value) in [('aa', 3), ('bb', 4), ('cc', 5)]:
        a.insert(key, value)
        print(a)

    print(a.lookup('cc'))
    a.insert('aa', 100)
    print(a)
