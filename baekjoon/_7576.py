from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
days = [[0 for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if (graph[i][j] == 1):  # 동시확산을 구현하기 위해 bfs 시작 시 모든 익은 토마토들을 큐에넣음
            q.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = dx[i]+x, dy[i]+y
        if (0 <= nx < n and 0 <= ny < m):  # nx는 행이므로 n(세로(행))의 범위에 포함되어야함 ny는 열이므로 m(가로(열))의 범위에 포함되어야함
            if (graph[nx][ny] == 0):
                graph[nx][ny] = 1
                days[nx][ny] = days[x][y] + 1
                q.append((nx, ny))

result = 0
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 0):
            print(-1)
            exit(0)
        result = max(result, days[i][j])
print(result)
