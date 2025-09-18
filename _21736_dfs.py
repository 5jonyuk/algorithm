import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
cnt = 0


def countingDfs(i, j):
    visited[i][j] = True
    global cnt
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    for x in range(4):
        ni = di[x]+i
        nj = dj[x]+j
        if (0 <= ni < n and 0 <= nj < m):
            if (campus[ni][nj] == 'O' and visited[ni][nj] == False):
                countingDfs(ni, nj)
            elif (campus[ni][nj] == 'P' and visited[ni][nj] == False):
                cnt += 1
                countingDfs(ni, nj)
            else:
                continue


found = 0
for i in range(n):
    for j in range(m):
        if (campus[i][j] == 'I'):
            countingDfs(i, j)
            found = 1
            break
    if (found == 1):
        break

if (cnt == 0):
    print('TT')
else:
    print(cnt)
