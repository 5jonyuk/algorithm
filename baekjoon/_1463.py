n = int(input())

numList = [0]*(n+1)


for i in range(2, n+1):
    numList[i] = numList[i-1]+1

    if (i % 2 == 0):
        numList[i] = min(numList[i], numList[i//2]+1)

    if (i % 3 == 0):
        numList[i] = min(numList[i], numList[i//3]+1)


print(numList[n])
