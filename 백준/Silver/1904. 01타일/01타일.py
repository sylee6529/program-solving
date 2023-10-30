import sys

n = int(sys.stdin.readline())


def get_tile(n):
    dp = [0, 1, 2] + [0] * (n - 2)

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 15746
    return dp[n]


print(get_tile(n))