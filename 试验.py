import j_共享栈模块 as j

j.push('spam')
j.push(12345)
print(j.top())
print(j.stack)
j.pop()
j.dump()

from j_多实例栈 import *

x = Stack2()
x.push('asfg')
x.push(111)
y = Stack2()
y.push(3.1415)
aaaa = x.reverse()
print(x)


from j_数据监控栈 import StackLog

x = StackLog()
y = StackLog()

for i in range(3): x.push(i)
for c in range(4): y.push(c)

print(f'{x}, , {y}')
print(f'{x.stats()}, {y.stats()}')


from j_元组树的栈 import Stack

x = Stack()
y = Stack()

for i in range(3): x.push(i)
for c in range(4): y.push(c)
print(f'{x}, , {y}')
print(x.pop())

from j_原地列表 import Stack3

x = Stack3()
x.push('ea')
print(x)