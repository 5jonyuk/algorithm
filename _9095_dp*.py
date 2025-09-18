n = int(input())

dp = [0]*11

for _ in range(n):
    x = int(input())

    for i in range(1, 11):
        if (i == 1):
            dp[i] = 1
        elif (i == 2):
            dp[i] = 2
        elif (i == 3):
            dp[i] = 4
        else:
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    print(dp[x])
