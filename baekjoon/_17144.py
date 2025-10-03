from sys import stdin
input = stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 공기청정기 위치 찾기
airCleaner = []
for i in range(R):
    if graph[i][0] == -1:
        airCleaner.append(i)
top = airCleaner[0]
bottom = airCleaner[1]

# 미세먼지 확산


def spreadDust():
    temp = [[0]*C for _ in range(R)]
    # 공기청정기 위치는 그대로
    temp[top][0] = temp[bottom][0] = -1

    for x in range(R):
        for y in range(C):
            if graph[x][y] > 0:  # 먼지가 있는 칸
                spread_amount = graph[x][y] // 5
                cnt = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        temp[nx][ny] += spread_amount
                        cnt += 1
                temp[x][y] += graph[x][y] - spread_amount * cnt
    return temp


# 공기청정기 작동
def airClean():
    # 위쪽 반시계
    for i in range(top-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for j in range(C-1):
        graph[0][j] = graph[0][j+1]
    for i in range(top):
        graph[i][C-1] = graph[i+1][C-1]
    for j in range(C-1, 1, -1):
        graph[top][j] = graph[top][j-1]
    graph[top][1] = 0

    # 아래쪽 시계
    for i in range(bottom+1, R-1):
        graph[i][0] = graph[i+1][0]
    for j in range(C-1):
        graph[R-1][j] = graph[R-1][j+1]
    for i in range(R-1, bottom, -1):
        graph[i][C-1] = graph[i-1][C-1]
    for j in range(C-1, 1, -1):
        graph[bottom][j] = graph[bottom][j-1]
    graph[bottom][1] = 0

    # 공기청정기 위치 보정
    graph[top][0] = -1
    graph[bottom][0] = -1


# 시뮬레이션
for _ in range(T):
    graph = spreadDust()
    airClean()

# 남은 미세먼지 합
answer = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)
