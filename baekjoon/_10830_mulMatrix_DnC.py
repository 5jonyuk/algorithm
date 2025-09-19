import sys
input = sys.stdin.readline

n, b = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]


def mul(A, B):
    mul_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul_matrix[i][j] += A[i][k] * B[k][j]
            mul_matrix[i][j] %= 1000
    return mul_matrix


def DnC(matrix, size):
    if (size == 1):
        # 곱셈 횟수가 1로 주어지고 행렬의 각 원소가 1000으로만 주어졌을 때 처리하기 위해
        return [[r % 1000 for r in row] for row in matrix]

    temp = DnC(matrix, size//2)

    if (size % 2 == 0):
        return mul(temp, temp)
    else:
        return mul(mul(temp, temp), matrix)


result = DnC(a, b)

for i in result:
    print(" ".join(map(str, i)))
