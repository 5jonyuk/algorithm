from math import gcd
import sys
input = sys.stdin.readline


def getNValue(num, exp):
    if (exp == 1):
        return num
    # 계산 도중 오버플로 방지하기위해 X로 모듈러 연산
    if (exp % 2 == 0):
        half = getNValue(num, exp//2)
        return half * half % X
    else:
        return num * getNValue(num, exp-1) % X


m = int(input())
X = int(1e9+7)
total = 0

for _ in range(m):
    N, S = map(int, input().split())

    # 기약분수로 표현하기 위해 최대공약수로 나눔
    g = gcd(N, S)
    N //= g
    S //= g

    # 페르마의 소정리: 모듈러에는 나눗셈이 없기 때문에 역원을 곱함
    # (a * b^(-1) = a * b^(X-2))mod X
    # total += S * pow(N, X-2, X) N을 X-2제곱하고 X로 나눈 나머지
    total += S * getNValue(N, X-2)

    # 항을 더할 때마다 모듈러 연산하여 overflow 방지 및 문제 요구 조건 만족
    total %= X

print(total)
