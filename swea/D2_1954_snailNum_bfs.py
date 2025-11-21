T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    graph = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    x, y = 0, -1  # 우로 시작하기 때문에 graph[0][0]을 채우기위해 -1로 시작
    d = 0

    while num <= (n * n):
        nx, ny = x + dx[d], y + dy[d]  # 일직선으로 가기위해 for문 4 하지않음
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            d = (d + 1) % 4  # dx, dy 인덱스 값을 1 -> 2 -> 3 -> 0 이 되도록, 일직선으로 가기위해 방향을 바꿀 때가 되면 바꿈

    print(f"#{tc}")
    for r in graph:
        print(*r, end=" ")
        print()
