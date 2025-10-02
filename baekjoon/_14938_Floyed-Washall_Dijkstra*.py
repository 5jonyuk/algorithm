'''
1. 노드들의 관계를 표현할 그래프 무한대로 초기화
2. 자기 자신으로 가는 간선들은 0 으로 초기화
3. 주어진 정보 입력
4. 최단거리 계산(플로이드-워셜) 점화식: d[i][j] = min(d[i][j], d[i][k]+d[k][j])
5. 출력
'''

import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
INF = int(1e9)

# 플로이드-워셜

# # 1.
# graph = [[INF]*(n+1) for _ in range(n+1)]

# # 2.
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if (i == j):
#             graph[i][j] = 0

# # 3.
# for _ in range(r):
#     a, b, l = map(int, input().split())
#     graph[a][b] = l
#     graph[b][a] = l

# # 4.
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if (i != j):
#                 graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# # 5.
# result = 0
# for i in range(1, n+1):
#     total = 0
#     for j in range(1, n+1):
#         if (graph[i][j] <= m):
#             total += items[j-1]
#     result = max(total, result)

# print(result)

# --------------------------------------------------------

# 다익스트라


def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # 거리, 노드

    while q:
        dist, currNode = heapq.heappop(q)

        if (dist > distance[currNode]):
            continue

        for nxt, cost in graph[currNode]:
            newCost = dist+cost
            if (distance[nxt] > newCost):
                distance[nxt] = newCost
                heapq.heappush(q, (newCost, nxt))
    return distance


graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# 출력
result = 0
for i in range(1, n+1):
    distance = dijkstra(i)
    total = 0
    for j in range(1, n+1):
        if (distance[j] <= m):
            total += items[j-1]
    result = max(total, result)

print(result)
