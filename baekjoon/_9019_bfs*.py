from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, end):
    q = deque([start])
    visited = [False] * 10000
    visited[start[0]] = True

    while q:
        num, cmd = q.popleft()

        if (num == end):
            print(cmd)
            break

        # D 연산
        D = (2*num) % 10000
        if (visited[D] == False):
            visited[D] = True
            q.append((D, cmd+"D"))

        # S 연산
        if (num == 0):
            S = 9999
        else:
            S = num - 1
        if (visited[S] == False):
            visited[S] = True
            q.append((S, cmd+"S"))

        # L 연산
        L = num // 1000 + (num % 1000)*10
        if (visited[L] == False):
            visited[L] = True
            q.append((L, cmd+"L"))

        # R 연산
        R = (num % 10)*1000 + num//10
        if (visited[R] == False):
            visited[R] = True
            q.append((R, cmd+"R"))


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    bfs((a, ""), b)
