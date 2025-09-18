import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

arr = []
'''
sys.stdin.readline:
버퍼에 더 이상 읽어들일 값이 없다면 빈 문자열 반환

input():
EOFERROR를 던져 예외처리 try-except 사용
'''
while True:
    x = input().strip()
    if (x == ''):
        break
    arr.append(int(x))


def postOrder(start, end):
    if (start > end):
        return
    root = arr[start]

    idx = start + 1
    while idx <= end and arr[idx] < root:
        idx += 1

    postOrder(start+1, idx-1)
    postOrder(idx, end)
    print(root)


postOrder(0, len(arr)-1)
