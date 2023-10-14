import math
import sys


def is_prime_number(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())

    for j in range(int(num/2), 1, -1):
        if is_prime_number(j) and is_prime_number(num - j):
            print(j, num - j)
            break