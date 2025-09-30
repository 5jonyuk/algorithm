from collections import deque
from collections import Counter
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = []


def bfs(start):
    INF = int(1e9)
    distance = [INF]*100001
    distance[start] = 0

    q = deque([start])

    while q:
        x = q.popleft()

        if (x == k):
            ans.append(distance[x])

        # # x-1
        # x_minus_1 = x-1
        # if (0 <= x_minus_1 < 100001 and distance[x_minus_1] >= distance[x]+1):
        #     distance[x_minus_1] = distance[x]+1
        #     q.append(x_minus_1)

        # # x+1
        # x_plus_1 = x+1
        # if (0 <= x_plus_1 < 100001 and distance[x_plus_1] >= distance[x]+1):
        #     distance[x_plus_1] = distance[x]+1
        #     q.append(x_plus_1)

        # # x*2
        # x_multiply_2 = x*2
        # if (0 <= x_multiply_2 < 100001 and distance[x_multiply_2] >= distance[x]+1):
        #     distance[x_multiply_2] = distance[x]+1
        #     q.append(x_multiply_2)

        for nx in [x-1, x+1, x*2]:
            if (0 <= nx < 100001):
                if (distance[nx] >= distance[x]+1):
                    distance[nx] = distance[x]+1
                    q.append(nx)


bfs(n)

ans = Counter(ans)
sortAns = sorted(ans.items(), key=lambda x: x[0])

for i in sortAns[0]:
    print(i)
