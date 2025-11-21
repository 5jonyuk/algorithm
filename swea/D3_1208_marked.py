T = 10
for tc in range(1, T+1):
    dumpCnt = int(input())
    boxes = list(map(int, input().split()))

    i = 1
    while i <= dumpCnt:
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        i += 1

    print(f"#{tc} {max(boxes)-min(boxes)}")
