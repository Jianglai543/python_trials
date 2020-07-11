from collections import OrderedDict


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
print(d)

"""用推导式删除键"""
c = {key:d[key] for key in d.keys() - {'bar','foo'}}
print(c)