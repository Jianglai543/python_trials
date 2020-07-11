x = 10
repr = """
z = 30
sum = x+z
print(sum)
print(3)
"""
def func():
    exec(repr)
    exec(repr, {'x':1, 'z':2})

func()

