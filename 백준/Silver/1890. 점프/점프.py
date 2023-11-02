import sys


n = int(sys.stdin.readline())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [list(0 for _ in range(n)) for _ in range(n)]
dx = [1, 0]
dy = [0, 1]


dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if n_list[i][j] == 0:
            continue
        if n_list[i][j] + i < n:
            dp[i + n_list[i][j]][j] += dp[i][j]
        if n_list[i][j] + j < n:
            dp[i][j + n_list[i][j]] += dp[i][j]
print(dp[n-1][n-1])