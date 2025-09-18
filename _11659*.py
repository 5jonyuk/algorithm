import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numList = list(map(int, input().split()))

sumList = [0]*len(numList)
sumList[0] = numList[0]
for i in range(1, len(numList)):
    sumList[i] = (numList[i]+sumList[i-1])

for _ in range(m):
    i, j = map(int, input().split())
    if (i == 1):
        print(sumList[j-1])
    else:
        print(sumList[j-1]-sumList[i-2])
