import heapq
import sys
input = sys.stdin.readline
n = int(input())

numheap = []
for _ in range(n):
    x = int(input())
    if (x == 0):
        if (len(numheap) == 0):
            print(0)
        else:
            print(heapq.heappop(numheap)[1])
    else:
        heapq.heappush(numheap, (abs(x), x))
