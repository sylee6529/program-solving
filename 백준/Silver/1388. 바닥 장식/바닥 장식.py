import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
adj_list = [list(sys.stdin.readline().strip()) for _ in range(r)]
visited = [[False for _ in range(c+1)] for _ in range(r+1)]

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    now = adj_list[x][y]

    # 문자 모양에 따라, 좌우 탐색할 건지, 상하 탐색할건지 정한다
    start, end = 0, 0
    if now == '-':
        start, end = 2, 3
    else:
        start, end = 0, 1

    while queue:
        x, y = queue.popleft()

        for i in range(start, end+1):
            nx, ny = x + dx[i], y + dy[i]

            # 밖이 아닌 경우
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == False:
                nn = adj_list[nx][ny]
                if now != nn:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
    cnt += 1
    return


for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            bfs(i, j)
print(cnt)