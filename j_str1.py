str = 'aaa,bbb cccccc;e;ddd,   e'
import re
strr = re.split(r'[;,\s]\s*', str)
print(strr)

strr2 = re.split(r'(;|,|\s)\s*', str)  # 捕获组， 带有分隔符号  ['aaa', ',', 'bbb', ' ', 'cccccc', ';', 'e', ';', 'ddd', ',', 'e']
strr3 = re.split(r'(?:;|,|\s)\s*', str) # not 捕获组
print(strr2)
print(strr3)