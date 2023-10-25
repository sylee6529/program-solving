import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(v+1)]
in_degree = [0] * (v+1)
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())

    edges[a].append(b)
    in_degree[b] += 1

# 진입 차수가 0인 사람들을 Queue에 삽입
queue = deque()
for i in range(1, v + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    p = queue.popleft()
    print(p, end=" ")
    for next in edges[p]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)
