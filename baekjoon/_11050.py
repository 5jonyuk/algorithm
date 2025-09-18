n, k = map(int, input().split())

#이항계수는 동적계획법으로...

# def combination(n, k):
#     if (n == k):
#         return 1
#     if (k == 1):
#         return n
#     if (n < k):
#         return 0
#     return combination(n-1, k-1)+combination(n-1, k)


# print(combination(n, k))

arr = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(min(i, k)+1):
        if (i == j or j == 0):
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

print(arr[n][k])
