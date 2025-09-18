import sys
input = sys.stdin.readline

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        # 가로 방향
        if (j+1 < n and house[i][j+1] == 0):
            dp[i][j+1][0] += dp[i][j][0]
        if (i+1 < n and j+1 < n and house[i][j+1] == 0 and house[i+1][j] == 0 and house[i+1][j+1] == 0):
            dp[i+1][j+1][2] += dp[i][j][0]
        # 세로 방향
        if (i+1 < n and house[i+1][j] == 0):
            dp[i+1][j][1] += dp[i][j][1]
        if (i+1 < n and j+1 < n and house[i][j+1] == 0 and house[i+1][j] == 0 and house[i+1][j+1] == 0):
            dp[i+1][j+1][2] += dp[i][j][1]
        # 대각선 방향
        if (j+1 < n and house[i][j+1] == 0):
            dp[i][j+1][0] += dp[i][j][2]
        if (i+1 < n and house[i+1][j] == 0):
            dp[i+1][j][1] += dp[i][j][2]
        if (i+1 < n and j+1 < n and house[i][j+1] == 0 and house[i+1][j] == 0 and house[i+1][j+1] == 0):
            dp[i+1][j+1][2] += dp[i][j][2]

print(dp[n-1][n-1][0]+dp[n-1][n-1][1]+dp[n-1][n-1][2])
