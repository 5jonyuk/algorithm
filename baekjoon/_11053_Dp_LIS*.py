import sys
input = sys.stdin.readline
n = int(input())
numList = list(map(int, input().split()))

dp = [1]*n  # 모든 수들은 자기 자신으로도 부분수열(길이가 1인)을 만들 수 있기에 1로 초기화

for i in range(1, n):
    for j in range(i):
        if (numList[i] > numList[j]):
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
