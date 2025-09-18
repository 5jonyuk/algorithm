from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())

numList = [int(input()) for _ in range(n)]


def ceiling(num):
    if (num >= 0):
        return int(num+0.5)
    else:
        return int(num-0.5)


def sansulavg():
    print(ceiling((sum(numList))/n))


def centerValue():
    numList.sort()
    print(numList[(len(numList)//2)])


def mode():
    numCounter = Counter(numList)
    most_common = numCounter.most_common()  # 카운터의 빈도 수 나열
    max_freq = most_common[0][1]  # 최대 빈도 수 선택

    most_numcandi = []

    # 카운터의 빈도 수 나열한 것 중에 최대 빈도 수와 같은 값 찾기
    for num, freq in most_common:
        if (freq == max_freq):
            most_numcandi.append(num)

    # 최대 빈도 수의 값이 1개보다 많을 경우 정렬 후 두번째값 추출
    if len(most_numcandi) > 1:
        most_numcandi.sort()
        print(most_numcandi[1])
    else:
        print(most_numcandi[0])


def numRange():
    print(max(numList)-min(numList))


sansulavg()
centerValue()
mode()
numRange()
