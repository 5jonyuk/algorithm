'''
다각형의 넓이 구하기 -> 신발끈 공식 사용
신발끈 공식: 1/2 * |(x1y2 + x2y3 + ... xny1) - (y1x2 + y2x3 + ynx1)|
'''

n = int(input())

xList = []
yList = []

for _ in range(n):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

leftResult = 0
rightResult = 0
for i in range(n):
    leftResult += xList[i]*yList[(i+1) % n]
    rightResult += yList[i]*xList[(i+1) % n]
print(round(((abs(leftResult-rightResult))/2), 2))
