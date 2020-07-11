def ins(seq1, seq2):
    res = []
    for i in seq1:
        if i in seq2:
            res.append(i)
    return res

def union(seq1, seq2):
    res = list(set(seq1))
    for i in seq2:
        if i not in res:
            res.append(i)
    return res

if __name__ == '__main__':
    s1 = "rtyui"
    s2 = 'cvbnmiiii'
    value = ins(s1, s2)
    value2 = union(s1, s2)
    print(value, value2)