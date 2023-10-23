import sys


v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

adj_list = [[] for _ in range(v+1)]
visited = []


def bfs(root):
    if root not in visited:
        visited.append(root)
        for i in adj_list[root]:
            bfs(i)
    return


for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


bfs(1)
print(len(visited) - 1)   # 자기자신인 1은 제외