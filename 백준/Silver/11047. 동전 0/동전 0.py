import sys

n, k = map(int, sys.stdin.readline().split())

n_list = [int(sys.stdin.readline()) for i in range(n)]

n_list.sort(reverse=True)
cnt = 0
for i in n_list:
    if i > k or k == 0:
        continue
    qt = k // i
    cnt += qt
    k -= i * qt

print(cnt)