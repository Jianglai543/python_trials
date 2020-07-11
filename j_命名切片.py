a = slice(0, 60, 1)
print(
    a.start,
    a.stop,
    a.step
)

s = 'helloworld'
print(a.indices(len(s)))  # (0, 10, 1)
for i in range(*a.indices(len(s))):   # *传递多个参数
    print(s[i])
