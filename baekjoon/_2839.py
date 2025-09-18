import sys
input = sys.stdin.readline
n = int(input())

i = 1
cnt = []
while n >= 5*i:
    if (n - 5*i) % 3 == 0:
        cnt.append(i + ((n - 5*i) // 3))
    i += 1
if (len(cnt) == 0 and n % 3 == 0):
    cnt.append(n//3)

if (len(cnt) == 0):
    print(-1)
else:
    print(min(cnt))
