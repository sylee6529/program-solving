import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, M+1):
            # 값이 coin 값보다 클 때만 기록한다
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])