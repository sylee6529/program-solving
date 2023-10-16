import sys

def hanoi(start, via, end, count):
    if count == 1:
        print("%d %d" % (start, end))
        return
    else:
        hanoi(start, end, via, count-1)
        print("%d %d" % (start, end))
        hanoi(via, start, end, count-1)


n = int(sys.stdin.readline())

print(2 ** n - 1)
if n <= 20:
    hanoi(1, 2, 3, n)