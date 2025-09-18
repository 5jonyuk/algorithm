from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]


def bfs(i, j):
    visited = [[False]*m for _ in range(n)]
    distance = [[0]*m for _ in range(n)]
    visited[i][j] = True
    distance[i][j] = 1
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()

        if (x == n-1 and y == m-1):
            return distance[x][y]

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < n and 0 <= ny < m):
                if (visited[nx][ny] == False and miro[nx][ny] == 1):
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))


print(bfs(0, 0))
