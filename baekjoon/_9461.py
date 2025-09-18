import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0]*(n+1)

    for i in range(1, n+1):
        if (i <= 3):
            dp[i] = 1
        else:
            dp[i] = dp[i-3]+dp[i-2]
    print(dp[n])
