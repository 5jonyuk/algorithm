T = int(input())

for tc in range(T):
    a, b, c = map(int, input().split())

    if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
        print("2")
    else:
        print("1")
