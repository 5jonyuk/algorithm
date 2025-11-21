T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    profit = 0
    max_sale_price = arr[-1]
    for i in range(n-2, -1, -1):
        if max_sale_price >= arr[i]:
            profit += max_sale_price - arr[i]
        else:
            max_sale_price = arr[i]
    print(f"#{tc} {profit}")
