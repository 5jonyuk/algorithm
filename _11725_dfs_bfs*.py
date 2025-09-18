from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

tree = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


def dfs(root):
    visited[root] = True
    for child in tree[root]:
        if (visited[child] == False):
            parent[child] = root
            dfs(child)


def bfs(root):
    q = deque([root])
    visited[root] = True

    while q:
        parentNode = q.popleft()
        for child in tree[parentNode]:
            if (visited[child] == False):
                visited[child] = True
                parent[child] = parentNode
                q.append(child)


dfs(1)
bfs(1)
for i in range(2, n+1):
    print(parent[i])
