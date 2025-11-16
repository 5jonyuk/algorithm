from enum import Enum


class alphabet(Enum):
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15


T = int(input())

for t in range(1, T + 1):
    n, num = input().split()

    result = []
    num: str
    for c in num:
        if c.isdigit():
            result.append(format(int(c), '04b'))
        else:
            result.append(format(alphabet[c].value, '04b'))

    print(f"#{t} {''.join(result)}")
