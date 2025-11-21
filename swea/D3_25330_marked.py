T = int(input())
for tc in range(1, T+1):
    S = input()
    flag = True
    pos_dict = {}

    for i, value in enumerate(S):
        if value not in pos_dict:
            pos_dict[value] = []
        pos_dict[value].append(i)

    for value, idxList in pos_dict.items():
        if len(idxList) == 2:
            distance = idxList[1] - idxList[0] - 1
            if (distance != int(value)):
                flag = False
                break
        elif len(idxList) != 0:
            flag = False
            break

    if flag:
        print("yes")
    else:
        print("no")
