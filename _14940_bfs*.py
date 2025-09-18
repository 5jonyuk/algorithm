from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

jido = [list(map(int, input().split())) for _ in range(n)]

ans = [[0 for _ in range(m)] for _ in range(n)]
target_i = 0
target_j = 0

for i in range(n):
    for j in range(m):
        if (jido[i][j] == 2):
            target_i = i
            target_j = j


def bfs(start):
    queue = deque([start])
    visited = [[False for _ in range(m)] for _ in range(n)]
    i, j = start
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < n and 0 <= ny < m):
                if (jido[nx][ny] == 1 and visited[nx][ny] == False):
                    visited[nx][ny] = True
                    ans[nx][ny] = ans[x][y] + 1
                    queue.append((nx, ny))


bfs((target_i, target_j))

for i in range(n):
    for j in range(m):
        if (jido[i][j] == 1 and ans[i][j] == 0):
            ans[i][j] = -1

for item in ans:
    print(*item)
