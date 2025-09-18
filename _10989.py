import sys
input = sys.stdin.readline
N = int(input())
numlist = [0]*10001

for _ in range(N):
    num = int(input())
    numlist[num] = numlist[num]+1

for i in range(1, len(numlist)):
    for j in range(numlist[i]):
        sys.stdout.write(str(i)+'\n')

# 내장 sort를 사용하지 않고 Counting Sort 사용
'''
1. sort()는 내부적으로 Timsort를 사용
Timsort는 파이썬의 정렬 알고리즘으로 효율적이지만,

입력 데이터 10^7개를 리스트에 저장하고 정렬하는 과정에서
정렬 중간에 추가 메모리 사용이 발생해요.

2. 입력 데이터를 모두 리스트에 넣으면 메모리 부담 큼
리스트 자체도 공간 차지

추가로 정렬 중 복사, 비교 등을 위한 임시 메모리도 추가로 소비

결국 256MB 제한을 넘을 수 있음

'''

'''
이 문제는 숫자의 범위가 작고(1~10,000), 입력 개수가 많을 때 사용하는 대표적 기법을 활용해야 해요:

카운팅 정렬(Counting Sort)
입력된 각 수의 등장 횟수를 세고,

해당 수를 등장 횟수만큼 출력하면 됨

시간 복잡도: O(N)

메모리: O(10001) → 매우 작음

'''
