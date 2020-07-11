stack = []

class error(Exception): pass

def push(obj):
    global stack
    stack = [obj], *stack

def pop():
    global stack
    if not stack:
        raise error('cannot pop')
    obj, *stack = stack
    return obj

def top():
    global stack
    if not stack:
        raise error('cannot get top')
    return stack[0]

def empty():
    return not stack

def member(it):
    return it in stack
def length():
    return len(stack)
def item(num):
    return stack[num]
def dump():
    print('<Stack:%s>' % stack)



