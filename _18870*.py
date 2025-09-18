import sys
input = sys.stdin.readline
n = int(input())
numList = list(map(int, input().split()))
setNumList = set(numList)
sortedSetNumList = sorted(setNumList)
numDict = {}
for i in range(len(sortedSetNumList)):
    numDict[sortedSetNumList[i]] = i

for i in numList:
    print(numDict[i], end=' ')
