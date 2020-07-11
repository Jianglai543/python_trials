class Node():
    def __init__(self, value):
        self.value = value
        self._children = []
        
    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, Node):
        self._children.append(Node)

    def __iter__(self):
        return iter(self._children)


class Node2():
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, Node):
        self._children.append(Node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for i in self:
            yield from i.depth_first()


if __name__ == '__main__':
    root = Node(3)
    child = Node(4)
    root.add_child(child)
    child2_1 = Node(5)
    root.add_child(child2_1)
    for ch in root:
        print(ch)
    print('\n')

    """Node 2"""
    root2 = Node2(3)
    child2_1 = Node2(4)
    root2.add_child(child2_1)
    child2_2 = Node2(5)
    root2.add_child(child2_2)
    child2_1.add_child(Node2(55))
    child2_1.add_child(Node2(66))
    child2_2.add_child(Node2(77))
    for ch in root2.depth_first():
        print(ch)
