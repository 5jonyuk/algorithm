import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

result = []

while True:
    common = set(A) & set(B)
    if (not common):
        break
    max_common = max(common)
    result.append(max_common)
    i = A.index(max_common)
    j = B.index(max_common)
    A = A[i+1:]
    B = B[j+1:]

print(len(result), end='\n')
print(*result)
