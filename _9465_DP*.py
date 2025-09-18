'''
예를들어  [0][3]에 도달하는 법은
1. [1][0] 부터 지그재그 
2. [0][0] 에서 한 번 가고 2열 건너뛰고 바로 3열로

때문에 [1][1]과 [1][2]만 고려하는 이유는 dp는 이미 그 전 값들을 포함하고 있으므로 이 둘만 생각하면 됨
'''
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    col = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    visited = [[False]*col for _ in range(2)]
    dp = [[0]*col for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if (col > 1):
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

        for i in range(2, col):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]

    print(max(dp[0][col-1], dp[1][col-1]))
