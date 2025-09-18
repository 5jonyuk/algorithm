N = int(input())
centerNum = 1
i = 1

while (N > centerNum):
    centerNum = centerNum + 6 * i
    i += 1

print(i)
