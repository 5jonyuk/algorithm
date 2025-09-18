import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)


def dijkstra(start):
    distance = [INF]*(V+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, k))

    while q:
        dist, currNode = heapq.heappop(q)

        if (dist > distance[currNode]):
            continue

        for nextNode, cost in graph[currNode]:
            newCost = dist+cost
            if (newCost < distance[nextNode]):
                distance[nextNode] = newCost
                heapq.heappush(q, (newCost, nextNode))

    return distance


distance = dijkstra(k)
for i in range(1, len(distance)):
    if (distance[i] == INF):
        print("INF")
    else:
        print(distance[i])
