import sys
input = sys.stdin.readline
n = int(input())

personList = [[0, 0] for _ in range(n)]
for i in range(n):
    age, name = map(str, input().split())
    personList[i][0] = int(age)
    personList[i][1] = name

# 순차정렬 시간복잡도 O(n^2)
# for i in range(len(personList)-1, 0, -1):
#     for j in range(i):
#         if (personList[j][0] > personList[j+1][0]):
#             personList[j], personList[j+1] = personList[j+1], personList[j]

# 내장 sort함수(Timsort) 시간복잡도(nlogn)
personList.sort(key=lambda x: x[0])

for age, name in personList:
    print(age, name)
