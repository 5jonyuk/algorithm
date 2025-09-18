from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs(node, visited):
    queue = deque([node])
    while queue:
        currentNode = queue.popleft()
        if (currentNode not in visited):
            visited.add(currentNode)
            print(currentNode, end=' ')
        for neighborNode in graph[currentNode]:
            if (neighborNode not in visited):
                queue.append(neighborNode)


def dfs(node, visited):
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if (neighbor not in visited):
            dfs(neighbor, visited)


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]


for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort()


dfsVisited = set()
dfs(v, dfsVisited)

print()

bfsVisited = set()
bfs(v, bfsVisited)
