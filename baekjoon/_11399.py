n = int(input())

timeList = list(map(int, input().split()))
timeList.sort()

time = 0
sumtime = 0
for i in range(n):
    time += timeList[i]
    sumtime += time
print(sumtime)
