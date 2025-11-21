# T = int(input())
#
#
# def check_row(arr):
#     if len(set(arr)) != 9:
#         return False
#     return True
#
#
# for tc in range(1, T + 1):
#     stoku = [(list(map(int, input().split()))) for _ in range(9)]
#     flag = True
#
#     for i in range(9):
#         flag = check_row(stoku[i])
#         if not flag:
#             break
#         col_List = []
#         for j in range(9):
#             col_List.append(stoku[j][i])
#         if len(set(col_List)) != 9:
#             flag = False
#             break
#
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             total=0
#             for k in range(i, i+3):
#                 for l in range(j, j+3):
#                     total += stoku[k][l]
#             if total != 45:
#                 flag = False
#                 break
#
#     if flag:
#         print(f"#{tc} 1")
#     else:
#         print(f"#{tc} 0")


T = int(input())


def check(arr):
    if len(set(arr)) != 9:
        return False
    return True


for tc in range(1, T + 1):
    stoku = [(list(map(int, input().split()))) for _ in range(9)]
    flag = True

    for i in range(9):
        if not check(stoku[i]):
            flag = False
            break
        if not check([col[i] for col in stoku]):
            flag = False
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [stoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(block)) != 9:
                flag = False
                break

    if flag:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
