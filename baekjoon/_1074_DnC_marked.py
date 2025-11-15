import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())

# arr = [[0 for _ in range(pow(2, n))] for i in range(pow(2, n))]
# count = -1


# def z(i, j, size):
#     global count
#     if (size == 2):
#         for x in range(i, i+size):
#             for y in range(j, j+size):
#                 arr[x][y] = count+1
#                 count += 1
#         return
#     else:
#         half = size // 2
#         z(i, j, half)
#         z(i, j+half, half)
#         z(i+half, j, half)
#         z(i+half, j+half, half)

count = 0


def z(x, y, size):
    global count
    if size == 1:
        if x == r and y == c:
            print(count)
            exit()

    half = size // 2

    # 1사분면
    if r < x + half and c < y + half:
        z(x, y, half)

    # 2사분면
    elif r < x + half and c >= y + half:
        count += half * half
        z(x, y + half, half)

    # 3사분면
    elif r >= x + half and c < y + half:
        count += 2 * (half * half)
        z(x + half, y, half)

    # 4사분면
    else:
        count += 3 * (half * half)
        z(x + half, y + half, half)


z(0, 0, pow(2, n))
# print(arr[r][c])
