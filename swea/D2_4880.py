import sys

sys.setrecursionlimit(10 ** 6)

T = int(input())


def fight(l, r):
    if matches[l] == 1 and matches[r] == 3:
        return l
    if matches[l] == 2 and matches[r] == 1:
        return l
    if matches[l] == 3 and matches[r] == 2:
        return l
    if matches[l] == matches[r]:
        return l
    return r


def dnc(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    left_player = dnc(start, mid)
    right_player = dnc(mid + 1, end)
    return fight(left_player, right_player)


for tc in range(1, T + 1):
    n = int(input())
    matches = list(map(int, input().split()))
    winner = dnc(0, n - 1)
    print(f"#{tc} {winner + 1}")
