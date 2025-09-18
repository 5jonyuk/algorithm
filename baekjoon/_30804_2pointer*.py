n = int(input())
fruitList = list(map(int, input().split()))
fruitCountDict = {}
left = fruitCnt = 0
fruit = 0

for right in range(n):
    if (fruitList[right] in fruitCountDict):
        fruitCountDict[fruitList[right]] += 1
    else:
        fruitCountDict[fruitList[right]] = 1
        fruitCnt += 1

    while fruitCnt > 2:
        fruitCountDict[fruitList[left]] -= 1
        if (fruitCountDict[fruitList[left]] == 0):
            del fruitCountDict[fruitList[left]]
            fruitCnt -= 1
        left += 1
    fruit = max(fruit, right - left + 1)

print(fruit)
