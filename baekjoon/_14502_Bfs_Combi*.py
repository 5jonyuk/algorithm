import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
blank = []
virus = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque(virus[:])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < n and 0 <= ny < m):
                if (temp_lab[nx][ny] == 0):
                    temp_lab[nx][ny] = 2
                    q.append((nx, ny))


# 빈 칸과 바이러스칸을 찾아서 배열에 넣음
for i in range(n):
    for j in range(m):
        if (lab[i][j] == 0):
            blank.append((i, j))
        elif (lab[i][j] == 2):
            virus.append((i, j))

max_safe = 0

# 조합으로 벽을 세울 빈 곳 찾기
for wall in combinations(blank, 3):
    # 연구소 복사
    temp_lab = copy.deepcopy(lab)
    # 복사 연구소에 벽 세우기
    for w in wall:
        temp_lab[w[0]][w[1]] = 1
    # 바이러스 퍼뜨리기
    bfs()
    # 각 로우마다 세이프존(0) 찾기
    safe = sum(row.count(0) for row in temp_lab)
    # 벽을 세운 조합 중 가장 많은 세이프존이 있는 것 찾기
    max_safe = max(safe, max_safe)

print(max_safe)
