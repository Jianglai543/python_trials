from collections import namedtuple

"""支持 len(), indexing, unpacking"""
sub = namedtuple('sub', ['addr', 'joined'])
sub_values = sub('0_value', '1_value')
print(sub_values)