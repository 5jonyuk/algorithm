T = int(input())
for tc in range(1, T+1):
    s = input()
    result = []
    for c in s:
        if not result:
            result.append(c)
        elif result[-1] != c:
            result.append(c)
        else:
            result.pop()
    print(f"#{tc} {len(result)}")
