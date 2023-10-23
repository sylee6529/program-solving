import sys

n = int(sys.stdin.readline())
adj_list = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(root):
    stack = [root]
    visited = [False for _ in range(n+1)]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for i in adj_list[node]:
                if parents[i] == 0:
                    parents[i] = node
                    stack.append(i)


dfs(1)
for i in parents[2:]:
    print(i)