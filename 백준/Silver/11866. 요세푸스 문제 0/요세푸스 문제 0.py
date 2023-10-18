import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())

deque = deque()

for i in range(1, n + 1):
    deque.append(i)

i = 1
print("<", end="")
while len(deque) > 0:
    if i % k == 0:
        print(deque.popleft(), end="")
        if len(deque) != 0:
            print(", ", end="")
    else:
        deque.rotate(-1)

    i += 1
print(">", end="")