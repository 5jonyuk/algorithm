# 도달하지 못했을 경우 0을 출력하는 형식때문에 개뻘짓함;;

T = int(input())

INF = int(1e9)
for tc in range(1, T+1):

    V, E = map(int, input().split())
    graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

    for i in range(1, V+1):
        for j in range(1, V+1):
            if (i == j):
                graph[i][j] = 0

    for i in range(E):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    s, g = map(int, input().split())

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if (graph[i][j] > graph[i][k]+graph[k][j]):
                    graph[i][j] = graph[i][k]+graph[k][j]

    if (graph[s][g] == INF):
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {graph[s][g]}")
#

# from collections import deque
# T = int(input())


# def bfs(start):
#     distance = [0] * (V+1)
#     visited = [False] * (V+1)
#     visited[start] = True
#     q = deque([start])

#     while q:
#         currNode = q.popleft()
#         if (currNode == g):
#             break
#         for nxtNode in graph[currNode]:
#             if not visited[nxtNode]:
#                 visited[nxtNode] = True
#                 distance[nxtNode] = distance[currNode] + 1
#                 q.append(nxtNode)
#     return (distance, visited)


# for tc in range(1, T+1):

#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]

#     for i in range(E):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)

#     s, g = map(int, input().split())

#     distance, visited = bfs(s)
#     if visited[g] == False:
#         print(f"#{tc} 0")
#     else:
#         print(f"#{tc} {distance[g]}")
