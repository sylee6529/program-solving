import sys


def pre_order(arr, root):
    if root == ".":
        return
    print(root, end="")
    pre_order(arr, arr[root][0])  # Left 노드 탐색
    pre_order(arr, arr[root][1])  # Right 노드 탐색


def in_order(arr, root):
    if root == ".":
        return

    in_order(arr, arr[root][0])  # Left 노드 탐색
    print(root, end="")
    in_order(arr, arr[root][1])  # Right 노드 탐색


def post_order(arr, root):
    if root == ".":
        return

    post_order(arr, arr[root][0])  # Left 노드 탐색
    post_order(arr, arr[root][1])  # Right 노드 탐색
    print(root, end="")


n = int(sys.stdin.readline())

binary_tree = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().rstrip().split()
    # root를 key로, 자식 노드를 value로 갖는 Dictionary
    binary_tree[root] = [left, right]


pre_order(binary_tree, "A")
print()
in_order(binary_tree, "A")
print()
post_order(binary_tree, "A")