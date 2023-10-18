import sys


def get_number(a, b, c):
    if b == 1:
        return a % c
    elif b == 0:
        return 1

    bn = get_number(a, b // 2, c)

    res = 0
    if b % 2 == 1:
        res = (bn * bn * (a % c)) % c
    else:
        res = bn * bn % c
    return res


a, b, c = map(int, sys.stdin.readline().split())


print(get_number(a, b, c))