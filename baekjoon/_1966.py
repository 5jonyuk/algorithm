from collections import deque

n = int(input())
for _ in range(n):
    cnt = 0
    quantity, currentIndex = map(int, input().split())
    importance = deque(map(int, input().split()))
    flagList = deque([0] * quantity)
    flagList[currentIndex] = True

    while importance:
        if importance[0] == max(importance):
            cnt += 1
            importance.popleft()
            target = flagList.popleft()
            if target == True:
                print(cnt)
                break
        else:
            importance.append(importance.popleft())
            flagList.append(flagList.popleft())
