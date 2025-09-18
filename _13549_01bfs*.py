from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())


def bfs(start):
    INF = int(1e9)
    dist = [INF] * 100001
    q = deque([start])
    dist[start] = 0

    while q:
        num = q.popleft()

        if (num == k):
            print(dist[num])
            return

        minusOne = num - 1
        if (0 <= minusOne < 100001 and dist[minusOne] > dist[num]+1):
            dist[minusOne] = dist[num] + 1
            q.append((minusOne))

        plusOne = num + 1
        if (0 <= plusOne < 100001 and dist[plusOne] > dist[num]+1):
            dist[plusOne] = dist[num] + 1
            q.append((plusOne))

        double = num * 2
        if (0 <= double < 100001 and dist[double] > dist[num]):
            dist[double] = dist[num]
            q.appendleft((double))


bfs(n)
