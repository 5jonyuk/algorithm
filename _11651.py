import sys
input = sys.stdin.readline
n = int(input())


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i][1] < right[j][1]):
            merged.append(left[i])
            i += 1
        elif (left[i][1] == right[j][1]):
            if (left[i][0] < right[j][0]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        else:
            merged.append(right[j])
            j += 1

    if (i == len(left)):
        merged.extend(right[j:])
    else:
        merged.extend(left[i:])

    return merged


xyList = []

for _ in range(n):
    x, y = map(int, input().split())
    xyList.append([x, y])

# xyList.sort(key=lambda x: (x[1], x[0]))

# for x, y in xyList:
#     print(x, y)

sortedXYList = merge_sort(xyList)

for x, y in sortedXYList:
    print(x, y)
