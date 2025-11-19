T = int(input())
for tc in range(1, T+1):
    n = int(input())

    n = n // 10
    dp = [0]*(n+1)

    dp[1] = 1
    dp[2] = 3

    if (n >= 3):
        for i in range(3, n+1):
            dp[i] = dp[i-2]*2 + dp[i-1]

    print(f"#{tc} {dp[n]}")
