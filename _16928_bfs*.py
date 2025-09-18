from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
move = {}

for _ in range(n+m):
    start, end = map(int, input().split())
    move[start] = end

dx = [1, 2, 3, 4, 5, 6]
visited = [False]*101
distance = [0]*101


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        x = q.popleft()

        for i in range(6):
            nx = dx[i]+x
            if (1 <= nx <= 100 and visited[nx] == False):
                if (nx in move):
                    visited[nx] = True
                    nx = move[nx]
                    if (visited[nx] == False):
                        visited[nx] = True
                        distance[nx] = distance[x]+1
                        q.append(nx)
                else:
                    visited[nx] = True
                    distance[nx] = distance[x]+1
                    q.append(nx)


bfs(1)
print(distance[100])
