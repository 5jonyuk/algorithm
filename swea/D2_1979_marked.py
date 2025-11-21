T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    cnt = 0

    # 가로 체킹
    for i in range(n):
        result_x = 0
        for j in range(n):
            if graph[i][j] == 0:
                if result_x == k:
                    cnt += 1
                    result_x = 0
                result_x = 0
            else:
                result_x += 1

        if result_x == k:
            cnt += 1

    # 세로 체킹
    for i in range(n):
        result_y = 0
        for j in range(n):
            if graph[j][i] == 0:
                if result_y == k:
                    cnt += 1
                    result_y = 0
                result_y = 0
            else:
                result_y += 1
        if result_y == k:
            cnt += 1

    print(f"#{tc} {cnt}")
