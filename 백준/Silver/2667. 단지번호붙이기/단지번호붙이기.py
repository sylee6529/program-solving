import sys
from collections import deque

n = int(sys.stdin.readline().strip())
adj_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

visited = [[False for _ in range(n+1)] for _ in range(n+1)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and adj_list[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt


estate_cnt_list = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and adj_list[i][j] == 1:
            estate_cnt_list.append(bfs(i, j))

estate_cnt_list.sort()

print(len(estate_cnt_list))
for i in estate_cnt_list:
    print(i)