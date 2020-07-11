def dedupe(items):
    """hashable!"""
    seen = set()
    for item in items:
        if item not in seen:
          yield item
          seen.add(item)


def dedupe2(items, key = None):
    """不可哈希如列表"""
    seen = set()
    for item in items:
        value = item if key == None else key(item)
        if value not in seen:
            yield item
            seen.add(value)


if __name__ == '__main__':
    items = [1,2,2,2,4,1,2,3,41,6]
    print(list(dedupe(items)))
    items2 = [{'x':1, 'y':2}, {'x':1, 'y':3}]
    print(list(dedupe2(items2, key = lambda d : d['x'])))