'''
다각형의 넓이 구하기 -> 신발끈 공식 사용
신발끈 공식: 1/2 * |(x1y2 + x2y3 + ... xny1) - (y1x2 + y2x3 + ynx1)|
'''
import sys
input = sys.stdin.readline

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

area = abs(leftResult-rightResult)/2
print(round(area, 2))  # 소수 둘째자리에서 반올림 후 첫째자리까지 출력
