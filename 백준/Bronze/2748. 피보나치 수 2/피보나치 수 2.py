import sys

n = int(sys.stdin.readline())
dp = [0, 1] + [0] * (n-1)


def fibo(n):
    if n <= 1:
        return n
    
    if dp[n] == 0:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]


print(fibo(n))