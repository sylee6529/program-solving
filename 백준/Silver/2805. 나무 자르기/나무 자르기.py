import sys


def search_height(arr, start, end, target):
    hsum = 0
    mid = (start + end) // 2

    left, right = start, end

    while left <= right:
        hsum = 0
        mid = (left + right) // 2  # 자를 높이
        for i in arr:
            if i > mid:
                hsum += i - mid

        if hsum > target:
            left = mid + 1
        elif hsum < target:
            right = mid - 1
        else:
            return mid
    return right


n, m = map(int, sys.stdin.readline().split())
height_list = []
height_list = list(map(int, sys.stdin.readline().split()))


print(search_height(height_list, 0, max(height_list), m))