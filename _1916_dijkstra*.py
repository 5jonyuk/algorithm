'''
다익스트라 알고리즘 
1. 시작 정점에서의 거리를 0, 나머지는 무한대로 설정
2. 현재 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택 -> 우선순위 큐(최소 힙)
3. 그 노드를 거쳐가는 경로가 더 짧으면 거리 갱신
4. 모든 노드가 처리될 때까지 반복
'''
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))   # 최소힙이므로 cost를 q[0]자리에 위치 (거리, 노드)

    while q:
        dist, currentNode = heapq.heappop(q)

        if (dist > distance[currentNode]):
            continue

        for nextNode, cost in graph[currentNode]:
            new_cost = dist + cost
            if (new_cost < distance[nextNode]):
                distance[nextNode] = new_cost
                # 최소힙이므로 cost를 q[0]자리에 위치
                heapq.heappush(q, (new_cost, nextNode))
    return distance


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

distance = dijkstra(start)
print(distance[end])
