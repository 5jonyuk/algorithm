T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    if (k <= 0 or n <= 0 or k >= 15 or n >= 15):
        break

    apt = [[0 for j in range(15)] for i in range(15)]

    # 반복문 방식
    # for i in range(1,15):
    #     apt[0][i] = i
    #     apt[i][1] = 1

    # for i in range (1,15):
    #     for j in range (1,15):
    #         apt[i][j] = apt[i-1][j] + apt[i][j-1]

    # 재귀방식
    def count(k, n):
        if (k == 0):
            return n
        if (n == 1):
            return 1
        if (apt[k][n] != 0):
            return apt[k][n]

        apt[k][n] = count(k-1, n) + count(k, n-1)

        return apt[k][n]

    print(count(k, n))
