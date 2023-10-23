import sys


v, e = map(int, sys.stdin.readline().split())
pnodes = [i for i in range(v+1)]


def find_parents(n):
    if pnodes[n] == n:
        return n
    pnodes[n] = find_parents(pnodes[n])
    return pnodes[n]


for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    ap = find_parents(a)
    bp = find_parents(b)

    if ap < bp: pnodes[bp] = ap
    else: pnodes[ap] = bp


result = []
for i in range(1, v + 1):
    result.append(find_parents(i))

cnt = len(set(result))

print(cnt)
