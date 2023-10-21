import sys


# Kruskal Algorithm 통한 구현
v, e = map(int, sys.stdin.readline().split())
edge_list = []          # (c, a, b) 형태로 저장
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edge_list.append((c, a, b))

parent_nodes = [i for i in range(v + 1)]
edge_list.sort()


def find_parent(x):
    # 본인이 부모 노드면 x 반환
    if x == parent_nodes[x]:
        return x
    # 본인이 부모 노드가 아니면, parent_nodes[x]에 parent_nodes[x]의 부모를 넣는다
    else:
        parent_nodes[x] = find_parent(parent_nodes[x])
        return parent_nodes[x]


def union_parent(x, y):
    xp = find_parent(x)
    yp = find_parent(y)

    if xp < yp:
        parent_nodes[yp] = xp
    else:
        parent_nodes[xp] = yp

min_cost = 0
for e in edge_list:
    # 부모 노드가 같지 않은지(사이클인지) 체크
    if find_parent(e[1]) != find_parent(e[2]):
        union_parent(e[1], e[2])
        min_cost += e[0]


print(min_cost)
