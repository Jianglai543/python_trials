"""same as string"""
data = bytearray(b'hello world')
print(data[0:5])
print(data.startswith(b'hello'))
print(data.split())
print(data.replace(b'world', b'jiang'))

import re

"""pattern as bytes"""
data2 = b'FOO:BAR, SPAM'
result = re.split(b'[:,]', data2)
print(result)
"""字符串格式化操作不适用字节串"""
print(
    '{:10s}{:10d}{:10.2f}'.format('abc', 100, 29.9).encode('ascii')
)

