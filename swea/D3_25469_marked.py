T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    cnt = 0
    grid = []

    rows = 0
    cols = 0

    rows_all_black = False
    # 행 체크
    for _ in range(h):
        s = input()
        grid.append(s)
        if s == '#' * w:
            rows += 1
        if rows == h:
            rows_all_black = True

    # 열 체크
    for i in range(w):
        all_black = True
        for j in range(h):
            if grid[j][i] != '#':
                all_black = False
                break
        if all_black:
            cols += 1

    if rows_all_black:
        print(min(rows, cols))
    else:
        print(rows+cols)
