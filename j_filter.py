def is_int(values):
    try:
        val = int(values)
        return True
    except:
        return False

if __name__ == '__main__':
    value = [1,2,'+', '-', 45,2,3,4,5]
    a = list(filter(is_int, value))  # filter true 加入
    print(a)