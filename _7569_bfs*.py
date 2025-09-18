from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())

graph = []
for _ in range(h):
    graph.append([list(map(int, input().split())) for _ in range(n)])

days = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

q = deque()

# 동시확산을 구현하기 위해 bfs 시작 시 모든 익은 토마토들을 큐에넣음
for z in range(h):
    for x in range(n):
        for y in range(m):
            if (graph[z][x][y] == 1):
                q.append((z, x, y))

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
while q:
    z, x, y = q.popleft()

    for i in range(6):
        nz, nx, ny = dz[i]+z, dx[i]+x, dy[i]+y

        # nx는 행이므로 n(세로(행))의 범위에 포함되어야함 ny는 열이므로 m(가로(열))의 범위에 포함되어야함
        if (0 <= nz < h and 0 <= nx < n and 0 <= ny < m):
            if (graph[nz][nx][ny] == 0):
                graph[nz][nx][ny] = 1  # 익음 표시 하면서 방문처리 역할
                days[nz][nx][ny] = days[z][x][y] + 1
                q.append((nz, nx, ny))

result = 0
for z in range(h):
    for i in range(n):
        for j in range(m):
            if (graph[z][i][j] == 0):
                print(-1)
                exit(0)
            result = max(result, days[z][i][j])
print(result)
