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



def build_per(fpexe):
    fplist = fpexe.split()
    stack = Stack()
    first = BinaryTree('')
    stack.push(first)
    current = first
    for i in fplist:
        if i == '(':
            pass
        if i not in  ['+', '-', '*', '/', '(', ')']:
            pass
        if i in ['+', '-', '*', '/']:
            pass
        if i == ')':
            pass
        else:
            raise ValueError
    return first
build_per('2 + 1')