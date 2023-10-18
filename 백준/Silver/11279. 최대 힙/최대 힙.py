import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
max_heap = []
for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0:    # pop
        if len(max_heap) == 0:
            print("0")
        else:
            print(-heappop(max_heap))
    else:
        heappush(max_heap, -num)
