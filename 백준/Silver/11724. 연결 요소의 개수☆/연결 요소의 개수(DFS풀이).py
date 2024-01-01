import sys


v, e = map(int, sys.stdin.readline().split())
cnt = 0
adj_list = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


def dfs(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            adj_list[node].sort(reverse=True)
            stack.extend(adj_list[node])


cnt = 0
for i in range(1, len(adj_list)):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
