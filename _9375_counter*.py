from collections import Counter
n = int(input())


for _ in range(n):
    clothTypeList = []
    sum = 1
    m = int(input())
    for _ in range(m):
        name, clothtype = input().split()
        clothTypeList.append(clothtype)
    counter_clothTypeList = Counter(clothTypeList)
    most_counter = counter_clothTypeList.most_common()

    for i in range(len(most_counter)):
        sum *= (most_counter[i][1] + 1)
    print(sum-1)
