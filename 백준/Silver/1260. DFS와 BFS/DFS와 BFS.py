import sys
from collections import deque


v, e, start_node = map(int, sys.stdin.readline().split())  # 정점, 간선, 탐색 시작 정점 번호

adj_list = [[] for _ in range(v + 1)]
for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(root):
    stack = [root]
    visited = [False for _ in range(v + 1)]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            adj_list[node].sort(reverse=True)
            stack.extend(adj_list[node])


def bfs(root):
    deq = deque()
    deq.append(root)

    visited = [False for _ in range(v + 1)]

    while deq:
        node = deq.popleft()
        if not visited[node]:
            visited[node] = True
            print(node, end=" ")
            adj_list[node].sort()
            deq.extend(adj_list[node])


dfs(start_node)
print()
bfs(start_node)