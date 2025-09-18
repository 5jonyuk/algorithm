n = int(input())

numList = [0]*(n+1)
for i in range(1, n+1):
    numList[i] = int(input())

dp = [0]*(len(numList))

if (n >= 1):
    dp[1] = numList[1]
if (n >= 2):
    dp[2] = numList[1]+numList[2]

for i in range(3, len(dp)):
    dp[i] = max(dp[i-2]+numList[i], dp[i-3]+numList[i-1]+numList[i])

print(dp[n])
