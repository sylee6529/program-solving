import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(r)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 밖이 아니고 칸이 1인 경우
            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
    return maze[r-1][c-1]


print(bfs(0, 0))
