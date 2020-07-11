class BinaryTree(object):

    def __init__(self, root):
        self.key = root
        self.left_tree = None
        self.right_tree = None

    def insert_left(self, new_node):
        if self.left_tree == None:
            self.left_tree = BinaryTree(new_node)
        else:
            new_branch = BinaryTree(new_node)
            new_branch.left_tree = self.left_tree
            self.left_tree = new_branch

    def insert_right(self, new_node_right):
        if self.right_tree == None:
            self.right_tree = BinaryTree(new_node_right)
        else:
            new_right = BinaryTree(new_node_right)
            new_right.right_tree = self.right_tree
            self.right_tree = new_right

    def get_right_child(self):
        return self.right_tree

    def get_left_child(self):
        return self.left_tree

    def get_root_val(self):
        return self.key

    def set_root_value(self, new_value):
        self.key = new_value

if __name__ == '__main__':
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.get_right_child().set_root_value('hello')
    r.get_left_child().insert_right('d')
