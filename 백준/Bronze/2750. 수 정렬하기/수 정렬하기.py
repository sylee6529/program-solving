import sys
n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(n_list):
    print(i)