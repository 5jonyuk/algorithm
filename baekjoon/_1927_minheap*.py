import heapq  # 우선순위 큐 숫자가 작은 것 부터 나오는 구조 => 최소힙
# 최대힙은 지원하지않아 음수로 저장 후 꺼낼 때 양수로 다시 꺼냄
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if (num == 0):
        if (len(heap) == 0):
            print(0)
            continue
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)
