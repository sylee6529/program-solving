import sys


def binary_search(arr, x):

    
    is_found = False
    left, right = 0, len(arr) - 1
    is_found = False

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()
for i in m_list:
    print(binary_search(n_list, i))