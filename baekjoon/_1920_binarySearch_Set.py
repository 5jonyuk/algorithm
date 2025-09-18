import sys
input = sys.stdin.readline
n = int(input())

a_list = list(map(int, input().split()))

m = int(input())

b_list = list(map(int, input().split()))

a_list.sort()

# 이진탐색은 정렬이 되어있는 상태여야함


def binary_search(left, right, key):

    if (left > right):
        print(0)
        return  # 아무 값도 반환하지않고 함수실행을 종료

    mid = (left+right) // 2

    if (key == a_list[mid]):
        print(1)
    elif (key < a_list[mid]):
        binary_search(left, mid-1, key)
    else:
        binary_search(mid+1, right, key)


for key in b_list:
    binary_search(0, len(a_list)-1, key)

# a_set = set(a_list)

# for item in b_list:
#     if item in a_set:
#         print(1)
#     else:
#         print(0)
