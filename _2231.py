N = int(input())

for i in range(1, N+1):
    nums = list(map(int, str(i)))
    M = sum(nums)+i
    if (M == N):
        print(i)
        break
    if (N == i):
        print(0)
