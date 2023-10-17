import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


sorted_list = []
sorted_list = selection_sort(n_list)
for i in sorted_list:
    print(i)
