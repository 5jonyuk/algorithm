from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start):
    visited = [[False for _ in range(n)] for _ in range(n)]
    i, j = start
    visited[i][j] = True
    q = deque([start])

    result = graph[n // 2][n // 2]

    while q:
        x, y = q.popleft()
        x, y = int(x), int(y)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if abs(nx - n // 2) + abs(ny - n // 2) <= n // 2:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        result += int(graph[nx][ny])
                        q.append((nx, ny))
    return result


for tc in range(1, T + 1):
    n = int(input())

    graph = [list(map(int, input().strip())) for _ in range(n)]

    answer = bfs((n // 2, n // 2))
    print(f"#{tc} {answer}")
