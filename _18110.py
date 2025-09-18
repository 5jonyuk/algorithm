import sys
input = sys.stdin.readline
n = int(input())


def ceiling(num):
    return int(num+0.5)


if (n == 0):
    print(0)

else:
    pointList = []
    for _ in range(n):
        pointList.append(int(input()))

    pointList.sort()
    percent15 = ceiling(n*0.15)

    if (percent15 > 0):
        pointList = pointList[percent15:-percent15]

    print(ceiling(sum(pointList)/len(pointList)))
