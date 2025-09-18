n, m = map(int, input().split())
ans = []


def backtrack(start):
    if (len(ans) == m):
        print(' '.join(map(str, ans)))
        return

    for i in range(start, n+1):
        ans.append(i)
        backtrack(i)
        ans.pop()


backtrack(1)
