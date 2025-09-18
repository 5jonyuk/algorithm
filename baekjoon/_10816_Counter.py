from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
myNumList = list(map(int, input().split()))

m = int(input())
numList = list(map(int, input().split()))

# myNumSet = set(myNumList)

# cnt = []
# for item in numList:
#     if (item in myNumSet):
#         cnt.append(myNumList.count(item))  # 시간초과 -> (count함수때문 리스트를 전부 순회함)
#     else:
#         cnt.append(0)

# for count in cnt:
#     print(count, end=' ')

# Counter를 사용하여 myNumList에 나오는 원소들의 갯수를 딕셔너리로 구성
myNumListCounter = Counter(myNumList)
# print(myNumListCounter)

for item in numList:
    print(myNumListCounter.get(item, 0), end=' ')  # none이면 0으로 출력
