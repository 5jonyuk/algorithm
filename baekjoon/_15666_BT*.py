import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
result = []
visited = [False]*n


# 바깥 반복문의 값을 고정한다는 것은 재귀 함수에 시작 인덱스를 같이 넘기는 것과 같다.
'''
i=0
    i=0
    i=1
    i=2
    i=3
i=1
    ...
'''


def backtrack(start):
    if (len(result) == m):
        print(' '.join(map(str, result)))
        return

    prev = -1
    for i in range(start, n):
        if (prev != numList[i]):
            result.append(numList[i])
            backtrack(i)
            result.pop()
            prev = numList[i]


backtrack(0)
