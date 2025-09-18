import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
nL = list(map(int, input().split()))
nL.sort()
result = []
visited = [False] * len(nL)


def dfs():
    if (len(result) == m):
        print(*result)
        return

    prev = -1
    for i in range(len(nL)):
        if (visited[i] == False and prev != nL[i]):
            result.append(nL[i])
            visited[i] = True
            dfs()
            result.pop()
            visited[i] = False
            prev = nL[i]


dfs()
