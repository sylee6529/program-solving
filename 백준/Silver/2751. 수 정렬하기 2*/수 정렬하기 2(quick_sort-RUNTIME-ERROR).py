import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left_arr, equal_arr, right_arr = [], [], []
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(left_arr) + equal_arr + quick_sort(right_arr)


sorted_list = []
sorted_list = quick_sort(n_list)
for i in sorted_list:
    print(i)
