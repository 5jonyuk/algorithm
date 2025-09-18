# 피보나치는 재귀로하면 시간이 많이 잡아먹음 그래서 동적계획법(반복법)으로 해결
# ex) 3은 1과 2의 값을 더한 값
import sys
input = sys.stdin.readline


def fibonacci(n):
    fibo = []

    fibo.append((1, 0))  # 0
    fibo.append((0, 1))  # 1

    if (n >= 2):
        for i in range(2, n+1):
            fibo.append((fibo[i-2][0]+fibo[i-1][0],
                        fibo[i-2][1]+fibo[i-1][1]))
        print(fibo[n][0], fibo[n][1])
    elif (n == 1):
        print(fibo[1][0], fibo[1][1])
    else:
        print(fibo[0][0], fibo[0][1])


t = int(input())
for i in range(t):
    n = int(input())
    fibonacci(n)
