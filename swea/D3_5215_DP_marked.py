T = int(input())


# 백트래킹
# def backtrack(idx, sumCal, sumPoint):
#     global answer

#     if sumCal > limitCal:
#         return

#     if idx == n:
#         answer = max(answer, sumPoint)
#         return

#     # idx번째 재료 포함했을 때
#     backtrack(idx+1, sumCal+graph[idx][1], sumPoint+graph[idx][0])

#     # idx번째 재료 포함 안했을 때
#     backtrack(idx+1, sumCal, sumPoint)


# for tc in range(1, T+1):
#     n, limitCal = map(int, input().split())
#     graph = []

#     for i in range(n):
#         point, cal = map(int, input().split())
#         graph.append((point, cal))

#     answer = 0
#     backtrack(0, 0, 0)

#     print(f"#{tc} {answer}")


# dp
for tc in range(1, T+1):
    n, limitCal = map(int, input().split())
    graph = []

    for i in range(n):
        point, cal = map(int, input().split())
        graph.append((point, cal))

    dp = [[0 for _ in range(limitCal+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        point, cal = graph[i-1]
        for j in range(limitCal+1):
            # i번째 재료 선택 안할 때
            dp[i][j] = dp[i-1][j]

            # i번째 재료 선택 할 때
            if j >= cal:
                dp[i][j] = max(dp[i][j], dp[i-1][j-cal] + point)

    print(f"#{tc} {dp[n][limitCal]}")
