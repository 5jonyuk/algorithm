a, b, c = map(int, input().split())


def DAC(a, b):
    if (b == 1):
        return a % c
    elif (b % 2 == 0):
        return pow(DAC(a, b//2), 2) % c
    else:
        return pow(DAC(a, b//2), 2) * a % c


print(DAC(a, b))
