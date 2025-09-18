n = int(input())

RGB = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0][0] = RGB[0][0]
dp[0][1] = RGB[0][1]
dp[0][2] = RGB[0][2]

for i in range(1, n):
    dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])  # RED
    dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])  # GREEN
    dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])  # BLUE

print(min(dp[n-1]))
