import heapq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    validation = [False] * k
    for i in range(k):
        cmd, num = input().strip().split()
        num = int(num)

        if (cmd == 'I'):
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            validation[i] = True
        else:
            if (num == -1):
                while (min_heap and validation[min_heap[0][1]] == False):
                    heapq.heappop(min_heap)
                if (min_heap):
                    validation[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            else:
                while (max_heap and validation[max_heap[0][1]] == False):
                    heapq.heappop(max_heap)
                if (max_heap):
                    validation[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    # 맨 앞에 validation이 False인 값이 있을 수 있으므로 최종으로 동기화
    while (min_heap and validation[min_heap[0][1]] == False):
        heapq.heappop(min_heap)
    while (max_heap and validation[max_heap[0][1]] == False):
        heapq.heappop(max_heap)

    if (min_heap and max_heap):
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
