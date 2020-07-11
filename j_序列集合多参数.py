def ins(*args):
    result = []
    res = list(set(args[0]))
    for i in res:
        for j in args[1:]:
            if i not in j:
                break
        else:
            result.append(i)
    return result

def union(*args):
    res = list(set(args[0]))
    for j in args[1:]:
        for k in j:
            if k not in res:
                res.append(k)

    return res

if __name__ == '__main__':
    s1 = "rtyui"
    s2 = 'cvbnmiiii'
    value = ins(s1, s2)
    value2 = union(s1, s2)
    print(value, value2)