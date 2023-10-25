import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = [[0] * (N + 1) for _ in range(N + 1)]
queue = deque()

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))
    indegree[X] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        result[i][i] = 1

while queue:
    now = queue.popleft()

    for i in graph[now]:
        next_node, num = i
        indegree[next_node] -= 1

        for j in range(1, N + 1):
            result[next_node][j] += result[now][j] * num

        if indegree[next_node] == 0:
            queue.append(next_node)

for i in range(1, N + 1):
    if result[N][i] != 0:
        print(i, result[N][i])