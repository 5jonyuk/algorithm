import sys
sys.setrecursionlimit(10**6)
t = int(input())


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y

        if (0 <= nx < m) and (0 <= ny < n):
            if (field[ny][nx] == 1):
                field[ny][nx] = -1
                dfs(nx, ny)


for _ in range(t):
    m, n, k = map(int, input().split())

    field = [[0 for _ in range(m)] for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    for x in range(m):
        for y in range(n):
            if (field[y][x] == 1):
                dfs(x, y)
                count += 1
    print(count)
