'''
1. 노드들의 관계를 표현할 그래프 무한대로 초기화
2. 자기 자신으로 가는 간선들은 0 으로 초기화
3. 주어진 정보 입력
4. 최단거리 계산(플로이드-워셜) 점화식: d[i][j] = min(d[i][j], d[i][k]+d[k][j])
5. 출력
'''

INF = float('inf')
n, m = map(int, input().split())

# 1.
graph = [[INF for _ in range(n+1)]for _ in range(n+1)]
# 2.
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == j):
            graph[i][j] = 0
# 3.
for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1
# 4.
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j):
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# 5.
ans = []
for i in range(1, n+1):
    sum = 0
    for j in range(1, n+1):
        sum += graph[i][j]
    ans.append((i, sum))

ans.sort(key=lambda x: (x[1]))
print(ans[0][0])

# bfs
# from collections import deque
# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]


# for _ in range(m):
#     i, j = map(int, input().split())
#     graph[i].append(j)
#     graph[j].append(i)


# def bfs(start):
#     visited = [False]*(n+1)
#     distance = [0]*(n+1)
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         current = queue.popleft()
#         for neighbor in graph[current]:
#             if (visited[neighbor] == False):
#                 visited[neighbor] = True
#                 distance[neighbor] = distance[current] + 1
#                 queue.append(neighbor)
#     return sum(distance)


# minValue = float('inf')
# result = 0
# for i in range(1, n+1):
#     total = bfs(i)

#     if (total < minValue):
#         minValue = total
#         result = i
# print(result)
