""" vars"""
s = '{name} has {n} messages.'
name = 'jone'
n = 20
print(s.format_map(vars()))
"""missing"""
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
del n
print(s.format_map(safesub(vars())))

"""函数 替换变量"""
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

print(sub('hi {name}'))
