import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))


def dfs(node, weight):
    visited[node] = True
    farthest = (weight, node)  # 가중치, 노드

    for nxt, w in tree[node]:
        if (visited[nxt] == False):
            candi = dfs(nxt, w+weight)
            if (candi[0] > farthest[0]):
                farthest = candi
    return farthest


visited = [False]*(n+1)
_, farthestNode = dfs(1, 0)
visited = [False]*(n+1)
diameter, _ = dfs(farthestNode, 0)

print(diameter)
