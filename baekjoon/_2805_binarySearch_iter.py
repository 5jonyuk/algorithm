import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))

tree.sort()


def check(mid):
    total = 0
    for i in range(len(tree)):
        if (tree[i]-mid > 0):
            total += (tree[i]-mid)
    if (total >= m):
        return 1
    else:
        return 0  # total < m 이라는 의미는 잘라낸 나무가 부족하다는 뜻 -> mid(height)가 너무 높다는 뜻


left = 1
right = tree[-1]
answer = 0

while (left <= right):
    mid = (left + right) // 2
    if (check(mid)):
        answer = mid  # 그래서 조건이 충족할 때만 answer를 갱신
        left = mid+1
    else:
        right = mid-1

print(answer)
