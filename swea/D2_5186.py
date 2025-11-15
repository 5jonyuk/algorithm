T = int(input())

for t in range(T):
    result = []
    N = float(input())

    while N != 0.0:
        N = 2 * N
        if N >= 1:
            result.append(int(N))
            N = N - 1
        else:
            result.append(0)

    binary_value = "".join(map(str, result))
    if len(binary_value) >= 13:
        print(f"#{t+1} overflow")
    else:
        print(f"#{t+1} {binary_value}")
