import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
minHeight = min(map(min, ground))  # ground의 각 행에서 최솟값을 뽑아낸 것 중에 가장 최솟값
maxHeight = max(map(max, ground))  # ground의 각 행에서 최댓값을 뽑아낸 것 중에 가장 최댓값

# 큰 수(무한대) 설정, 주로 최솟값 구할 때 사용 최댓값 구할때는 -inf 음의 무한대 사용
result_time = float('inf')
result_height = 0

for height in range(minHeight, maxHeight+1):
    time = 0
    b_temp = b
    for i in range(n):
        for j in range(m):
            if (ground[i][j] < height):  # 땅의 블럭 값이 목표값보다 작다면 추가
                b_temp -= (height-ground[i][j])
                time += (height-ground[i][j])
            else:  # 땅의 블럭 값이 목표값보다 크다면 제거
                b_temp += (ground[i][j]-height)
                time += 2*(ground[i][j]-height)
    if (b_temp >= 0):  # b_temp 가 음수가 된다면 안되는 케이스라 판단
        if (time < result_time or (time == result_time and height > result_height)):
            result_time = time
            result_height = height
print(result_time, result_height)
