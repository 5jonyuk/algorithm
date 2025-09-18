n, k = map(int, input().split())

numList = [i for i in range(1, n+1)]
yosepusList = []
index = 0
for _ in range(n-1):
    index = (index+k-1) % len(numList)
    yosepusList.append(numList.pop(index))
yosepusList.append(numList[0])

print('<'+', '.join(map(str, yosepusList)) + '>')
# map()은 반복문 없이 빠르게 숫자로 이루어진 리스트를 문자열 리스트로 변환하는 함수
# .join()은 문자열 리스트를 하나의 문자열로 묶어주는 함수
