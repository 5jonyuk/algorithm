import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 모든 수들은 자기 자신으로도 부분수열(길이가 1인)을 만들 수 있기에 1로 초기화
dp_up = [1]*n
dp_down = [1]*n

# 증가하는 방향은 앞에서 시작해서 기준(i) 보다 비교 대상들(j)이 작을 때만 추가
for i in range(1, n):
    for j in range(i):
        if (arr[i] > arr[j]):
            dp_up[i] = max(dp_up[j]+1, dp_up[i])

# 감소하는 방향은 뒤에서 시작해서 기준(i) 보다 비교 대상들(j)이 작을 때만 추가
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if (arr[i] > arr[j]):
            dp_down[i] = max(dp_down[j]+1, dp_down[i])

result = 0
for i in range(n):
    # 빼기 1은 자기 자신을 빼는 것
    # 예) 1 5 2 1 4 3 4 5 2 1 입력에서
    # 인덱스 2 (5)의 기준에서 보았을 때
    # 증가하는 값 1, 5
    # 감소하는 값 5, 4, 3, 2, 1 이므로
    # 자기 자신 -1하는 것임
    result = max(dp_up[i]+dp_down[i]-1, result)
print(result)
