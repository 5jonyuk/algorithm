from collections import deque
T = int(input())


def bfs(start, end):
    q = deque([start])

    while q:
        currNode = q.popleft()

        for nxtNode in graph[currNode]:
            if nxtNode == end:
                return True
            q.append(nxtNode)
    return False


for tc in range(1, T+1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        s, e = map(int, input().split())
        graph[s].append(e)

    S, G = map(int, input().split())

    if bfs(S, G):
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
