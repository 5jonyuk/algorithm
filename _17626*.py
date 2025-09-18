# import sys
# input = sys.stdin.readline
# n = int(input())

# dp = [50001]*(n+1)

# for i in range(1, len(dp)):
#     if (i <= 3):
#         dp[i] = i
#     elif (i == 4):
#         dp[i] = 1
#     else:
#         for j in range(1, int(i**0.5)+1):
#             dp[i] = min(dp[i], dp[i-j*j]+1)

# print(dp[n])

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] + [50001] * n

for i in range(1, n+1):
    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j*j] + 1)

print(dp[n])
