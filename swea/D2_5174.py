def dfs(n):
    global cnt
    for child in graph[n]:
        if not child:
            return
        cnt += 1
        dfs(child)


T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    graph = [[] for _ in range(e+2)]
    eList = list(map(int, input().split()))

    for i in range(0, len(eList), 2):
        graph[eList[i]].append(eList[i+1])

    cnt = 1
    dfs(n)
    print(f"#{tc} {cnt}")
