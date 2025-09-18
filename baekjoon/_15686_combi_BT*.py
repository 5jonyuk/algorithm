# 조합
# from itertools import combinations
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(n)]

# houses = []
# chickens = []
# for i in range(n):
#     for j in range(n):
#         if (graph[i][j] == 0):
#             continue
#         elif (graph[i][j] == 1):
#             houses.append((i, j))
#         else:
#             chickens.append((i, j))

# nCr = list(combinations(chickens, m))

# ans = []

# for chicken in nCr:
#     chickendistanse = 0
#     for houses_x, houses_y in houses:
#         result = int(1e9)
#         for selected_chicken_x, selected_chicken_y in chicken:
#             result = min(abs(houses_x-selected_chicken_x) +
#                          abs(houses_y-selected_chicken_y), result)
#         chickendistanse += result
#     ans.append(chickendistanse)

# print(min(ans))

# 백트래킹
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if (city[i][j] == 0):
            continue
        elif (city[i][j] == 1):
            houses.append((i, j))
        else:
            chickens.append((i, j))


def calc_cityChickenDistance(selected):
    cityChickenDistance = 0
    for houses_x, houses_y in houses:
        chickenDistance = int(1e9)
        for selected_chicken_x, selected_chicken_y in selected:
            chickenDistance = min(chickenDistance, abs(selected_chicken_x - houses_x) +
                                  abs(selected_chicken_y - houses_y))
        cityChickenDistance += chickenDistance
    return cityChickenDistance


def backtrack(idx, selected):
    global ans

    # 선택된 치킨집이 m개가 되면 계산 -> 이 부분이 백트래킹
    if (len(selected) == m):
        ans = min(ans, calc_cityChickenDistance(selected))
        return ans

    # 종료조건
    if (idx == len(chickens)):
        return

    # 현재 치킨집 선택
    # +를 써서 리스트를 추가하면 selected 원본은 유지되면서 새로 호출할 땐 확장된 리스트가 넘어감
    # append() 후 pop() 하는 과정을 안하려고 사용
    backtrack(idx+1, selected+[chickens[idx]])

    # 현재 치킨집 선택 x
    backtrack(idx+1, selected)


backtrack(0, [])
print(ans)
