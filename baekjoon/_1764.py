import sys
input = sys.stdin.readline
n, m = map(int, input().split())

nolistenpersonList = [input().strip() for _ in range(n)]
noseepersonList = [input().strip() for _ in range(m)]

nolistenpersonSet = set(nolistenpersonList)
noseepersonSet = set(noseepersonList)

nolistenseepersonSet = nolistenpersonSet.intersection(noseepersonList)

print(len(nolistenseepersonSet))
sortednolistenseepersonSet = sorted(nolistenseepersonSet)
for person in sortednolistenseepersonSet:
    print(person)
