T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    graph = []
    for x in range(n):
        graph.append(list(map(int, input().split())))

    # ========= 반복문 ========= #
    # answer = 0
    # for i in range(n):
    #     for j in range(n):
    #         result = 0
    #         for k in range(i, i + m):
    #             for g in range(j, j + m):
    #                 if 0 <= k < n and 0 <= g < n:
    #                     result += graph[k][g]
    #                 else:
    #                     continue
    #         answer = max(answer, result)
    #
    # print(f"#{tc} {answer}")

    # ========= 누적합 ========= #
    ps = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # 누적합 채우기
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ps[i][j] = graph[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]

    answer = 0
    for k in range(n - m + 1):
        for l in range(n - m + 1):
            result = (ps[k + m][l + m] - ps[k][l + m] - ps[k + m][l] + ps[k][l])
            answer = max(answer, result)

    print(f"#{tc} {answer}")
