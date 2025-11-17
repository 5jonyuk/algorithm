from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start):
    a, b = start
    q = deque([start])
    visited = [[False] * n for _ in range(n)]
    visited[a][b] = True

    while q:
        x1, y1 = q.popleft()
        for i1 in range(4):
            nx, ny = dx[i1] + x1, dy[i1] + y1
            if 0 <= nx < n and 0 <= ny < n:
                if miro[nx][ny] == '3':
                    return True
                if not visited[nx][ny] and miro[nx][ny] == '0':
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False


for tc in range(1, T + 1):
    n = int(input())
    miro = [input() for _ in range(n)] # 문자열로 입력받은 거 주의
    x = y = 0
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if miro[i][j] == '2':
                x, y = i, j
                break

    is_dochak = bfs((x, y))
    if is_dochak:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
