from collections import namedtuple
import re

"""havenot understand yet!"""

NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
"""scanner = master_pat.scanner('foo = 42')
print(scanner.match())"""




def generate_token(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text) # 返回一个scanner对象， 在上面一次一次match
    for m in iter(scanner.match, None): # None 为停止标志
        yield Token(m.lastgroup, m.group())


for tok in generate_token(master_pat, 'foo = 42'):
    print(tok)
