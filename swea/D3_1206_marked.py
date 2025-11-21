T = 10
for tc in range(1, T+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        if (buildings[i] > buildings[i-1]) and (buildings[i] > buildings[i-2]) and (buildings[i] > buildings[i+1]) and (buildings[i] > buildings[i+2]):
            left = min(buildings[i] - buildings[i-1],
                       buildings[i] - buildings[i-2])
            right = min(buildings[i] - buildings[i+1],
                        buildings[i] - buildings[i+2])
            result += min(left, right)
    print(f"#{tc} {result}")
