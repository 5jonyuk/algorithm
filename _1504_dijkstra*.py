import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # (거리,노드)

    while q:
        dist, currNode = heapq.heappop(q)

        if (dist > distance[currNode]):
            continue

        for nextNode, value in graph[currNode]:
            newValue = dist + value
            if (newValue < distance[nextNode]):
                distance[nextNode] = newValue
                heapq.heappush(q, (newValue, nextNode))

    return distance


n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

INF = int(1e9)

dist = dijkstra(1)  # 1에서 모든 정점경로
v1_dist = dijkstra(v1)  # v1에서 모든 정점경로
v2_dist = dijkstra(v2)  # v2에서 모든 정점경로

v1_path = dist[v1]+v1_dist[v2]+v2_dist[n]
v2_path = dist[v2]+v2_dist[v1]+v1_dist[n]

result = min(v1_path, v2_path)

if (result < INF):
    print(result)
else:
    print(-1)
