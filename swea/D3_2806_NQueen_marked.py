T = int(input())


def check(row):
    for r in range(row):
        if queen[row] == queen[r] or abs(row - r) == abs(queen[row] - queen[r]):
            return False
    return True


def backtrack(row):
    global cnt

    if row == n:
        cnt += 1
        return

    for col in range(n):
        queen[row] = col
        if check(row):
            backtrack(row + 1)


for tc in range(1, T + 1):
    n = int(input())
    queen = [0] * n
    cnt = 0

    backtrack(0)

    print(f"#{tc} {cnt}")
