n = int(input())

physicalList = [[0, 0] for _ in range(n)]

for i in range(n):
    weight, height = map(int, input().split())
    physicalList[i][0] = weight
    physicalList[i][1] = height

rank = [0]*n

for i in range(n):  # 각 사람 i에 대해서
    count = 0
    for j in range(n):  # 다른 사람 j를 다 비교
        if i == j:
            continue
        if physicalList[i][0] < physicalList[j][0] and physicalList[i][1] < physicalList[j][1]:
            count += 1
    rank[i] = count + 1

for i in rank:
    print(i, end=' ')
