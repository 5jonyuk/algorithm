import sys
sys.setrecursionlimit(10**9)
n = int(input())

star = [[' ']*n*2 for _ in range(n)]


def starFunc(i, j, size):
    if (size == 3):
        star[i][j] = '*'
        star[i+1][j-1] = star[i+1][j+1] = '*'
        for k in range(-2, 3):
            star[i+2][j+k] = '*'
    else:
        newSize = size // 2
        starFunc(i, j, newSize)  # 위
        starFunc(i+newSize, j-newSize, newSize)  # 왼쪽 아래
        starFunc(i+newSize, j+newSize, newSize)  # 오른쪽 아래


starFunc(0, n-1, n)

for i in star:
    print("".join(i))
