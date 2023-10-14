import sys

n = int(sys.stdin.readline())

for i in range(n):
    num, st = sys.stdin.readline().split()

    result = ""

    for s in st:
        result += s * int(num)

    print(result)