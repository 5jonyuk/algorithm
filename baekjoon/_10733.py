import sys
input = sys.stdin.readline  # 개행문자 \n까지 포함

n = int(input())  # int가 묵시적으로 개행문자 무시하고 int로 변환하여 문제 x

numList = []

for _ in range(n):
    num = int(input())
    if (num == 0):
        numList.pop()
    else:
        numList.append(num)
print(sum(numList))
