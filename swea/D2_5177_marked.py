

T = int(input().strip())


def swap(arr, i):
    temp = arr[i]
    arr[i] = arr[i//2]
    arr[i//2] = temp
    return arr


for t in range(T):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    min_heap = [0]
    for i in arr:
        min_heap.append(i)
        idx = len(min_heap)-1
        while idx > 1:
            if (min_heap[idx] < min_heap[idx//2]):
                swap(min_heap, idx)
            idx = idx//2

    result = 0
    while n > 1:
        n = n//2
        result += min_heap[n]
    print(f"#{t+1} {result}")
