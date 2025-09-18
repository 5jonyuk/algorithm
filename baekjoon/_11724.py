import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if (visited[next] == False):
            dfs(next)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if (not visited[i]):
        dfs(i)
        count += 1

print(count)
