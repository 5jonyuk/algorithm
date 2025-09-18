# import time
# start_time = time.time()  # 시작 시간

# n, m = map(int, input().split())
# for i in range(n, m+1):
#     for j in range(2, i+1):
#         if (i % j == 0):
#             if (i == j):
#                 print(i)
#             else:
#                 break

# end_time = time.time()  # 끝 시간

# print(f"걸린 시간: {end_time - start_time:.4f}초")

import math


n, m = map(int, input().split())
primeList = [True for _ in range(m+1)]
primeList[0] = False
primeList[1] = False

for i in range(2, int(math.sqrt(m))+1):
    if (primeList[i] == True):
        j = 2
        while i*j <= m:
            primeList[i*j] = False
            j += 1

for i in range(n, m+1):
    if (primeList[i] == True):
        print(i)


'''
에라토스테네스의 체 알고리즘
1. 2부터 N까지의 모든 자연수를 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다. i는 소수
3. 남은 수 중에서 i의 배수를 모두 제거 한다.
4. 더 이상 반복할 수 없을 때까지 2,3번 반복
'''
