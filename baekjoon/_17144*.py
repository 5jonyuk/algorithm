import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
airCleaner = []
for i in range(R):
    if (graph[i][0] == -1):
        airCleaner.append(i)
top = airCleaner[0]
bottom = airCleaner[1]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def spreadMisemunzis():  # 미세먼지 확산
    temp = [[0]*C for _ in range(R)]
    temp[top][0] = temp[bottom][0] = -1

    for x in range(R):
        for y in range(C):
            if (graph[x][y] > 0):
                cnt = 0
                for i in range(4):
                    nx, ny = dx[i]+x, dy[i]+y
                    if (0 <= nx < R and 0 <= ny < C):
                        if (temp[nx][ny] != -1):
                            temp[nx][ny] += graph[x][y] // 5
                            cnt += 1
                temp[x][y] += graph[x][y] - (graph[x][y] // 5) * cnt
    return temp


def airClean():  # 공기청정기 가동
    # 위쪽 반시계방향
    for i in range(top-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for j in range(C-1):
        graph[0][j] = graph[0][j+1]
    for k in range(top):
        graph[k][C-1] = graph[k+1][C-1]
    for r in range(C-1, 1, -1):
        graph[top][r] = graph[top][r-1]
    graph[top][1] = 0

    # 아래쪽 시계방향
    for i in range(bottom+1, R-1):
        graph[i][0] = graph[i+1][0]
    for j in range(C-1):
        graph[R-1][j] = graph[R-1][j+1]
    for k in range(R-1, bottom, -1):
        graph[k][C-1] = graph[k-1][C-1]
    for r in range(C-1, 1, -1):
        graph[bottom][r] = graph[bottom][r-1]
    graph[bottom][1] = 0

    # 공기청정기 위치 보장
    graph[top][0] = -1
    graph[bottom][0] = -1


for _ in range(T):
    graph = spreadMisemunzis()
    airClean()

result = 0
for row in graph:
    sum = 0
    for r in row:
        if (r != -1):
            sum += r
    result += sum
print(result)
