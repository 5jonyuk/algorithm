import sys
input = sys.stdin.readline

n = int(input())

numList = []
for i in range(n):
    num = int(input())
    numList.append(num)

numList.sort()

for i in range(len(numList)):
    print(numList[i])
