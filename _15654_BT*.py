n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
ans = []
visited = [False]*10001


def backtrack():
    if (len(ans) == m):
        print(' '.join(map(str, ans)))
        return

    for i in numList:
        if (visited[i] == False):
            ans.append(i)
            visited[i] = True
            backtrack()
            s = ans.pop()
            visited[s] = False


backtrack()
