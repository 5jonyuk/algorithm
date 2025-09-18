from collections import deque
n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(start, normal):
    q = deque([start])
    i, j = start
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = dx[k]+x, dy[k]+y
            if (0 <= nx < n and 0 <= ny < n):
                if (normal == True):
                    if (graph[nx][ny] == graph[x][y] and visited[nx][ny] == False):
                        visited[nx][ny] = True
                        q.append((nx, ny))
                else:
                    if (graph[x][y] == 'R' or graph[x][y] == 'G'):
                        if ((graph[nx][ny] in ('R', 'G')) and visited[nx][ny] == False):
                            visited[nx][ny] = True
                            q.append((nx, ny))
                    else:
                        if (graph[nx][ny] == graph[x][y] and visited[nx][ny] == False):
                            visited[nx][ny] = True
                            q.append((nx, ny))


cnt = 0
normal = True
for i in range(n):
    for j in range(n):
        if (visited[i][j] == False):
            bfs((i, j), normal)
            cnt += 1
print(cnt, end=' ')

cnt = 0
visited = [[False for _ in range(n)] for _ in range(n)]
normal = False

for i in range(n):
    for j in range(n):
        if (visited[i][j] == False):
            bfs((i, j), normal)
            cnt += 1
print(cnt)


# dfs

# import sys
# sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제
# n = int(input())
# graph = [list(input().strip()) for _ in range(n)]
# visited = [[False for _ in range(n)] for _ in range(n)]

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]


# def dfs(x, y, normal):
#     visited[x][y] = True
#     for k in range(4):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#             if normal:
#                 if graph[nx][ny] == graph[x][y]:
#                     dfs(nx, ny, normal)
#             else:
#                 if graph[x][y] in ('R', 'G'):
#                     if graph[nx][ny] in ('R', 'G'):
#                         dfs(nx, ny, normal)
#                 else:
#                     if graph[nx][ny] == graph[x][y]:
#                         dfs(nx, ny, normal)


# # 일반 시야
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             dfs(i, j, True)
#             cnt += 1
# print(cnt, end=' ')

# # 적록색약 시야
# visited = [[False for _ in range(n)] for _ in range(n)]
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             dfs(i, j, False)
#             cnt += 1

# print(cnt)
