import sys
input = sys.stdin.readline
n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x: (x[1], x[0]))

cnt = 0
temp = meet[0][1]
for i in range(1, len(meet)):
    if (temp <= meet[i][0]):
        cnt += 1
        temp = meet[i][1]

# print(cnt+1)
print(meet)
