N = int(input())
size = list(map(int, input().split()))
T_count = 0
if (sum(size) == N):
    T, P = map(int, input().split())
    for i in range(len(size)):
        if (size[i] % T != 0):
            T_count += int(size[i]/T + 1)
        else:
            T_count += int(size[i]/T)
    P_quotient = int(N/P)
    P_remainder = int(N % P)
print(T_count)
print(P_quotient, P_remainder)
