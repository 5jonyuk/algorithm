t = int(input())
for _ in range(t):
    cnt = 0
    A, B, N = map(int, input().split())
    x = A
    y = B

    while (x <= N and y <= N):
        if (x > y):
            y += x
        else:
            x += y
        cnt += 1

    print(cnt)
