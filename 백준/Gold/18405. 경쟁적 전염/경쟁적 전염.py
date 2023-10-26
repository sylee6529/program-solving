import sys
from collections import deque
from heapq import heappop, heappush

r, c = map(int, sys.stdin.readline().split())
adj_list = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
s, x, y = map(int, sys.stdin.readline().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


virus_list = []
for i in range(r):
    for j in range(r):
        if adj_list[i][j] != 0:
            heappush(virus_list, (adj_list[i][j], i, j))


def bfs(a, b, num):
    queue = deque()
    queue.append((a, b))
    tmp = []

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]

            if 0 <= na < r and 0 <= nb < r and adj_list[na][nb] == 0:
                # queue.append((na, nb))
                adj_list[na][nb] = num
                heappush(tmp, (adj_list[na][nb], na, nb))

    return tmp


for _ in range(s):
    sum_tmp_list = []
    while virus_list:
        v_num, row, col = heappop(virus_list)
        tmp = bfs(row, col, v_num)
        sum_tmp_list.extend(tmp)
    virus_list = sum_tmp_list

print(adj_list[x-1][y-1])