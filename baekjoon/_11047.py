import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coinList = [int(input()) for _ in range(n)]
cnt = 0

for i in range(len(coinList)-1, -1, -1):
    if (coinList[i] > k):
        continue
    else:
        while (k >= coinList[i]):
            # k -= coinList[i]
            # cnt += 1
            cnt = cnt + (k // coinList[i])
            k = k % coinList[i]


print(cnt)
