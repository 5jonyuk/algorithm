n = int(input())

arr = [i for i in range(1, n + 1)]

for num in arr:
    cnt = 0
    temp = num
    while num > 0:
        r = num % 10
        if r == 3 or r == 6 or r == 9:
            cnt += 1
        num = num // 10

    if cnt == 0:
        print(temp, end=' ')
    else:
        print("-" * cnt, end=' ')
