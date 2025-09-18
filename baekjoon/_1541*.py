query = input().split('-')

sumList = []
for item in query:
    sum = 0
    itemList = item.split('+')
    for item2 in itemList:
        sum += int(item2)
    sumList.append(sum)

sum2 = sumList[0]
for i in range(1, len(sumList)):
    sum2 -= sumList[i]
print(sum2)
