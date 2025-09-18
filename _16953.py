from collections import deque
a, b = map(int, input().split())


def bfs(x, c):
    q = deque([(x, c)])

    while q:
        x, c = q.popleft()

        if (x == b):
            print(c)
            return  # bfs함수 자체를 종료한다

        mul2 = x*2
        if (mul2 <= b):
            q.append((mul2, c+1))

        right1 = int(str(x)+'1')
        if (right1 <= b):
            q.append((right1, c+1))

    print(-1)


bfs(a, 1)
