import re

"""find"""
text1 = '1990/2/1abcdefg2090/12/1'
datapat = re.compile(r'\d+/\d+/\d+')  # 将格式编译
if datapat.match(text1):    # 对格式进行匹配
    print('yes')
print(datapat.findall(text1))

datapat = re.compile(r'(\d+)/(\d+)/(\d+)')

for m in datapat.finditer(text1):
    print(m.groups())  # 一个一个的，组成元组
"""replace"""
print(datapat.sub(r'\3-\1-\2', text1))
from calendar import month_abbr
def change_month(m):
    mon = month_abbr[int(m.group(3))]
    return '{}-{}-{}'.format(m.group(2), mon, m.group(1))


print(datapat.sub(change_month, text1))  # 定义函数以修改格式
newtext, n = datapat.subn(r'\3-\1-\2', text1)  # 替换结果，匹配个数
print(newtext)
print(n)