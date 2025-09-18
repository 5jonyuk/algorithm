'''
1. 문제에서 인덱스가 1부터 시작 (주의)

2. 2차원 배열의 부분합 = 구하려는 위치의 실제값 + 실제 값에 위쪽 dp값 + 실제 값에 왼쪽 dp 값 - 겹치는 왼쪽 위 대각선
ex)
1 2    
3 4 => 4 + 1+2 + 1+3 - 1

3. 답을 구할 때는 전체 부분합 - 구하려는 사각형의 제외한 사각형 + 겹치는 부분
ex)
1 2 3 4
2 3 4 5   => (1,1) ~ (2,3) / dp[2][3] - dp[0][3] - [2][0] + dp[0][0]
3 4 5 6
정답을 구할 때 인덱스들은 구하려는 사각형을 기준으로 인덱스 구하기
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nList = [list(map(int, input().split())) for _ in range(n)]
mList = [list(map(int, input().split())) for _ in range(m)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = nList[0][0]

if (n > 1):
    for i in range(n):
        for j in range(n):
            if (i == 0 and j == 0):
                continue
            elif (i == 0):
                dp[i][j] = nList[i][j] + dp[i][j-1]
            elif (j == 0):
                dp[i][j] = nList[i][j] + dp[i-1][j]
            else:
                dp[i][j] = nList[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for x1, y1, x2, y2 in mList:
    result = dp[x2-1][y2-1]
    if (x1 > 1):
        result -= dp[x1-2][y2-1]
    if (y1 > 1):
        result -= dp[x2-1][y1-2]
    if (x1 > 1 and y1 > 1):
        result += dp[x1-2][y1-2]
    print(result)
