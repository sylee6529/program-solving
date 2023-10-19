import sys


n = int(sys.stdin.readline())

new_num, origin_n, cnt = 0, n, 1
left, right = 0, 0
while True:
    left = n % 10
    right = (n // 10 + n % 10) % 10
    new_num = left * 10 + right
    if origin_n == new_num:
        break
    n = new_num
    cnt += 1

print(cnt)