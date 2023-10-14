import sys

n_list = [int(sys.stdin.readline()) for _ in range(9)]

max_num = max(n_list)
print(max_num)
print(n_list.index(max_num) + 1)
