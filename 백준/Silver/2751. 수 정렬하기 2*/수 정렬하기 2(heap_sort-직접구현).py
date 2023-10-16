import sys

n = int(sys.stdin.readline())
n_list = [int(sys.stdin.readline()) for _ in range(n)]


def heap_sort(arr):
    n = len(arr)
    arr = [0] + arr     # index를 1부터 시작하기 위해 0 삽입

    sorted_list = []
    for i in range(n//2, 0, -1):  # Leaf node를 제외한, 자식노드를 가진 노드들을 순회한다
        heapify(arr, i, n)

    for i in range(n, 0, -1):
        sorted_list.append(arr[1])
        arr[i], arr[1] = arr[1], arr[i]
        heapify(arr, 1, i-1)
    return sorted_list


def heapify(arr, idx, n):
    left = idx * 2
    right = idx * 2 + 1
    s_idx = idx

    # 부모와 2 자식노드 중 작은 값은을 찾음
    if left <= n and arr[s_idx] > arr[left]:
        s_idx = left
    if right <= n and arr[s_idx] > arr[right]:
        s_idx = right

    # 선택 노드와 자식 노드의 위치가 바뀌어야 한다면
    if s_idx != idx:
        arr[idx], arr[s_idx] = arr[s_idx], arr[idx] # 부모노드 <->자식노드
        return heapify(arr, s_idx, n)


sorted_list = []
sorted_list = heap_sort(n_list)
for i in sorted_list:
    print(i)
