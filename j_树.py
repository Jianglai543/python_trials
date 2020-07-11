def binary_tree(root):
    return [root, [], []]

def insert_left(root, newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root

def insert_write(root, newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root

def root_left_child(root):
    return root[1]

def get_root_val(root):
    return root[0]

def set_root_val(root, new_root):
    root[0] = new_root

if __name__ == '__main__':
    r = binary_tree(3)
    insert_left(r, 5)
    l = root_left_child(r)
    print(l)