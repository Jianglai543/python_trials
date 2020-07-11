from collections import defaultdict


d = defaultdict(list)

pairs = {}
pairs.setdefault('a', []).append(1)
pairs.setdefault('a', []).append(3)
pairs.setdefault('c', []).append(3)
print(pairs)


for key, value in pairs.items():
    d[key].append(value)

print(d)



