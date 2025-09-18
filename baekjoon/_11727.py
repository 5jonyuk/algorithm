n = int(input())

numList = [0]*(n+1)
numList[1] = 1

for i in range(2, len(numList)):
    if (i % 2 == 0):
        numList[i] = numList[i-1]*2+1
    else:
        numList[i] = numList[i-1]*2-1
print(numList[n] % 10007)
