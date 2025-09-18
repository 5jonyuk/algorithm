n = int(input())


def Paper(x, y, size):
    global whiteCnt
    global blueCnt

    standardColor = colorPaper[x][y]
    all_same = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if (colorPaper[i][j] != standardColor):
                all_same = False
                break

    if (all_same):
        if standardColor == 0:
            whiteCnt += 1
        else:
            blueCnt += 1
        return  # 현재 함수호출을 끝내고 현재호출 부른 곳으로 돌아간 후 다음 단계 시작

    half = size // 2
    Paper(x, y, half)
    Paper(x+half, y, half)
    Paper(x, y+half, half)
    Paper(x+half, y+half, half)


whiteCnt = 0
blueCnt = 0

colorPaper = [list(map(int, input().split())) for _ in range(n)]

Paper(0, 0, n)

print(whiteCnt)
print(blueCnt)
