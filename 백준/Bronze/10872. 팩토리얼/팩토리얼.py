import sys


def factorial(num):
    if num <= 1:
        return 1;
    return num * factorial(num-1)


n = int(sys.stdin.readline())

print(factorial(n))
