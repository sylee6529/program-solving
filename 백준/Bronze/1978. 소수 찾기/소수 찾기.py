import math
import sys


def is_prime_number(a):
    if a == 1:
        return False
    for i in range(2, int(math.sqrt(a)+1)):
        if a % i == 0:
            return False
    return True


n = int(sys.stdin.readline())
num_list = []
num_list.extend(list(map(int, input().split())))

sum1 = 0
for i in num_list:
    if is_prime_number(i):
        sum1 += 1
print(sum1)