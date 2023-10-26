import sys

N, K = map(int, sys.stdin.readline().split())
weights = [0]
values = [0]


def knapsack(W, wts, vals, n):  # W: 배낭의 무게한도, n: 보석의 수
    dp = [[0 for x in range(W + 1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            # w가 i번째 보석의 무게 이상일 경우 (보석을 넣을 수 있는 경우)
            elif w >= wts[i]:       # 이전 보석을 빼고 현재 보석을 넣은 가치와 이전 보석이 가진 가치를 비교
                dp[i][w] = max(dp[i-1][w - wts[i]] + vals[i], dp[i-1][w])
            else:       # 보석을 넣을 수 없는 경우, 이전 보석의 가치를 그대로 넣는다
                dp[i][w] = dp[i-1][w]
    return dp[n][W]


for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    weights.append(w)
    values.append(v)


print(knapsack(K, weights, values, N))