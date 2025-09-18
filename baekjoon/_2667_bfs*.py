'''
1. 주어진 정보 입력
2. (0,0)부터 1인지 탐색
3. 1인 곳 찾으면 bfs로 탐색
4. 찾을 때마다 단지카운팅 1증가
5. 끊어지면 반복문으로 다음 단지 찾기
'''
from collections import deque


def bfs(i, j):
    visited[i][j] = True
    queue = deque([(i, j)])
    apartCnt = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < n and 0 <= ny < n):
                if (visited[nx][ny] == False and apartMap[nx][ny] == 1):
                    visited[nx][ny] = True
                    apartCnt += 1
                    queue.append((nx, ny))
    return apartCnt  # 큐가 끝났다는 건 한 단지 탐색 끝났다는 것


n = int(input())

apartMap = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dangeList = []

for i in range(n):
    for j in range(n):
        if (visited[i][j] == False and apartMap[i][j] == 1):
            apartCount = bfs(i, j)
            dangeList.append(apartCount)

dangeList.sort()
print(len(dangeList))

for i in dangeList:
    print(i)
