T = int(input())

for tc in range(1, T+1):
    heights = list(map(int, input().split()))
    max_h = max(heights)
    check = False

    i = max_h+1
    while True:
        if (sum(heights)+i) % 7 == 0:
            print(i)
            break
        i += 1
