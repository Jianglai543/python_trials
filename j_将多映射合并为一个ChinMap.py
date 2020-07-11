from collections import ChainMap

a = {'x' : 1,'y' : 3}
b = {'z' : 2,'y' : 4}
c = ChainMap(a, b)


len_c=len(c)
list_c = list(c.keys())
list_c2 = list(c.values())
print(
    len_c,
    list_c,
    list_c2
)