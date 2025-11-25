T = 10
for tc in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    flag = 0
    for i in range(n):
        for j in range(n):
            if graph[j][i] == 1:
                flag = 1
            elif graph[j][i] == 2 and flag == 1:
                cnt += 1
                flag = 0

    print(f"#{tc} {cnt}")

