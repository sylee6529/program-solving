import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]


def heap_sort(arr):
    heap = []
    for num in arr:
        heappush(heap, num)

    sorted_list = []
    while heap:
        sorted_list.append(heappop(heap))
    return sorted_list


sorted_list = []
sorted_list = heap_sort(n_list)
for i in sorted_list:
    print(i)
