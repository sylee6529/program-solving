import sys


cnt = 0
N = int(sys.stdin.readline())
col = [-1] * N


def n_queen(num, col):
    global cnt

    if num == N:
        cnt += 1
        return

    for i in range(N):
        col[num] = i

        if promising(num, col):
            n_queen(num + 1, col)


def promising(r, col):
    k = 0
    flag = True
    while k < r and flag:
        if col[r] == col[k] or abs(col[r] - col[k]) == (r - k):
            return False
        k += 1
    return True


n_queen(0, col)
print(cnt)
