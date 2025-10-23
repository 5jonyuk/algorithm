import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))

INF = int(1e9)


def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, currNode = heapq.heappop(q)

        if (dist > distance[currNode]):
            continue

        for nxtNode, cost in graph[currNode]:
            newCost = dist+cost
            if (newCost < distance[nxtNode]):
                distance[nxtNode] = newCost
                heapq.heappush(q, (newCost, nxtNode))
    return distance


partyVillage = dijkstra(x)

result = 0
for i in range(1, n+1):
    if (i == x):
        continue
    minGoToPartyVillage = dijkstra(i)[x]
    result = max(result, minGoToPartyVillage + partyVillage[i])

print(result)
