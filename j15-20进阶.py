"""
import heapq
list1 = [1,2,3,4,5]

value = {key for key in list1 if key > 3}
print(value)

dictionaty = {
    'aaa' : 123,
    'bbb' : 345,
    'ccc' : 567
}
# .items()
value2 = {key : value for key, value in dictionaty.items() if value < 300}
print(heapq.nlargest(2, {value for value in dictionaty.items() }))
print(value2)
"""



"""
import heapq
list1 = ['a', 'b', 'c', 'd','e']
list2 = ['yuwen', 'shuxue', 'yingyu']
list_all = [[None] * len(list1) for _ in range(len(list2))]
print(list_all)
new_list_all = []
for indexes, values in enumerate(list1):
    for indexes2, values2 in enumerate(list2):
        grade = 1   #  int(input('>>'))
        list_all[indexes2][indexes] = grade
        list_all[1][0] = 3
        print(f'{indexes2},{indexes}')
print(heapq.nlargest(1, list_all[1]))
print(list_all)

"""

import itertools

"""for i in itertools.permutations('abcd'):
    print(i)
total = 0
for i in itertools.combinations('abcde', 3):
    total += 1
    print(i)
print(total)
for i in itertools.cycle(('a','b','c')):
    print(i)
list = []
for i in itertools.product(range(2), repeat=4):
    list.append(i)
print(list)
for i in itertools.product('abcd','xy', repeat=1):
    print(i)
natural = itertools.count(1)
for i in itertools.takewhile(lambda x : x<=10, natural):
    print(i)"""


from collections import namedtuple, deque, OrderedDict, defaultdict, Counter

"""name = namedtuple('name', ('x', 'y'))
p = name(1, 2)
print(p)
list = [1,2,3,4]
dq = deque()
dq.extend(list)
dq.append(2)
dq.append(3)
dq.appendleft(5)
dq.pop()
dq.popleft()
print(dq)

diction3 = OrderedDict([('a', 3), ('f', 2), ('c', 1)])
print(diction3)

values = [1,2,3]
dict1 = defaultdict(list)

for i in values:
    if i < 2:
        dict1['k1'].append(i)
    else:
        dict1['k2'].append(i)
print(dict1)


dd = defaultdict()
dd['a'] = 3
dd['b'] = 4
print(dd)"""


def order(list, comp = lambda x, y : x<y):

    for i in range(len(list)-1):

        for j in range(i, len(list)):
            if comp(list[j], list[i]):
                list[i], list[j] = list[j], list[i]

    return list



def order2(list, comp = lambda x, y : x<y):

    for i in range(len(list)-1):

        for j in range(0, len(list)-1-i):

            if comp(list[j+1], list[j]):
                list[j+1], list[j] = list[j], list[j+1]

    return list


def order3(list, comp = lambda x, y : x<y):
    for i in range(len(list)-1):
        swap = False
        for j in range(0, len(list) - i - 1):
            if comp(list[j+1], list[j]):
                swap = True
                list[j+1], list[j] = list[j], list[j+1]
        if swap:
            swap = False
            for jj in range(len(list)-2-i, i, -1):
                if comp(list[jj + 1], list[jj]):
                    swap = True
                    list[jj + 1], list[jj] = list[jj], list[jj + 1]
        elif not swap:
            break
    return list

def merge(list1, list2, comp = lambda x, y : x < y):
    i = 0
    j = 0
    list = []
    while True:
        if comp(list1[i], list2[j]):
            list.append(list1[i])

            if i == len(list1)-1:
                list.extend(list2[j:])
                return list
            else:
                i += 1
        else:
            list.append(list2[j])
            if j == len(list2)-1:
                list.extend(list1[i:])
                return list
            else:
                j += 1


def merge(items1, items2, comp=lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    print(items1, items2)
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def find_line(list, key):
    for index, value in enumerate(list):
        if value == key:
            return index
    return 0


def bin_search(list, key):
    start, end = 0, len(list) - 1
    while start <= end:
        mid = list[(start + end) // 2]

        if key < mid:
            end = (start + end) // 2 - 1
        elif key > mid:
            start = (start + end) // 2 + 1
        else:
            return (start + end) // 2
    return -2


def j100_100():
    for i in range(20):
        for j in range(33):
            k = 100 - i - j
            if i * 5 + j * 3 + k // 3 == 100 and k % 3 == 0:
                print(i, j, k)


def fish_devided():
    fish = 6

    while True:
        total = fish
        devided = True
        for _ in range(2):
            if (total - 1) % 5 == 0 :
                total = (total-1) // 5 * 4
            else:
                devided = False
                break
        if devided:
            print(fish)
            return fish
        fish += 5


def fish():
    fishs = 6
    enough = False
    while not  enough:
        total = fishs
        x = 0
        for _ in range(5):

            if (total - 1) % 5 != 0 :
                enough = False
                x = 0
                break
            else:
                total = (total-1) // 5 * 4
                x += 1
                if x == 5:
                    print(fishs)
                    return fishs
        fishs += 5

import heapq
def greedy(*args):
    return args[0][0], int(args[0][1]), int(args[0][2]), int(args[0][1])//int(args[0][2])


def greedy2():
    item, value, item_weight = input('$$').split()
    return item, value, item_weight


def greedy3():
    max_weight, number = map(int, input('>>').split())
    stolen_diction = dict()
    all_things = []
    for i in range(number):
        item_name, item_value, item_weight, value_per_weight = greedy(greedy2())
        diction1 = dict()
        diction1['name'] = item_name
        diction1['value'] = item_value
        diction1['weight'] = item_weight
        diction1['per_weight'] = value_per_weight
        all_things.append(diction1)
        print(all_things)
    total_weight = 0
    total_value = 0

    for _ in range(number):
        if total_weight < max_weight:
            list3 = heapq.nlargest(1, all_things, key= lambda x : x['per_weight'])
            for item2 in list3: value_it = item2['item_value']
            for item2 in list3: weight_it = item2['item_weight']
            name = stolen_diction['name']
            total_value += value_it
            total_weight += weight_it


if __name__ == '__main__':
    """list = [3,7,4,6,2,5]
    print(order3(list))"""
    list1 = [0,2,3,4,4,4,5]
    list2 = [1,3,3]
   # print(merge(list1, list2))# success
   # print(merge_sort(list1)) 没看太懂
   # print(bin_search(list1, 3))  二分法傻
  #  j100_100()  背的对了
   # fish() # ok
    greedy3()



