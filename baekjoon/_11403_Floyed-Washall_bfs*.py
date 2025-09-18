import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = [list(map(int, input().strip().split())) for _ in range(n)]

# 플로이드-워셜
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if (graph[i][k] and graph[k][j]):
#                 graph[i][j] = 1

# for i in graph:
#     print(*i)  # *i는 i가 리스트일 때 리스트 내부 요소들을 공백을 두고(언패킹하여) 출력한다는 뜻

# '''
# [1, 1, 1]       1 1 1
# [1, 1, 1]  ->   1 1 1
# [1, 1, 1]       1 1 1
#     i            *i
# '''

# bfs
ans = [[0 for _ in range(n)] for _ in range(n)]


def bfs(start):
    visited = [0 for _ in range(n)]
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for i in range(n):
            if (visited[i] == 0 and graph[current][i] == 1):
                queue.append(i)
                visited[i] = 1
                ans[start][i] = 1


for i in range(n):
    bfs(i)

for i in ans:
    print(*i)
