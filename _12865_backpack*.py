n, k = map(int, input().split())

item = []
for _ in range(n):
    w, v = map(int, input().split())
    item.append((w, v))

item.sort()
dp = [[-1 for _ in range(k+1)] for _ in range(n+1)]


def backpack(n, k):
    if (n == 0 or k == 0):
        return 0
    if dp[n][k] != -1:  # 메모이제이션 -> 다른 경로에서 다시 만난 경우 그대로 값을 사용
        return dp[n][k]
    if (k >= item[n-1][0]):  # 배낭의 무게보다 아이템 무게가 작을 때
        dp[n][k] = max(
            backpack(n-1, k),
            item[n-1][1] + backpack(n-1, k - item[n-1][0])
        )
    else:  # 배낭의 무게보다 아이템 무게가 클 때
        dp[n][k] = backpack(n-1, k)

    return dp[n][k]


print(backpack(n, k))
