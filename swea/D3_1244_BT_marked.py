

def dfs(arr, exchangeCnt):
    global answer

    if exchangeCnt == exchange:
        answer = max(answer, int("".join(arr)))
        return

    state = ("".join(arr), exchangeCnt)

    # 가지치기
    if state in visited:
        return

    visited.add(state)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(arr, exchangeCnt+1)
            arr[j], arr[i] = arr[i], arr[j]


T = int(input())

for tc in range(1, T+1):
    num_str, exchange = map(str, input().split())
    exchange = int(exchange)

    arr = list(num_str)
    visited = set()
    answer = 0

    dfs(arr, 0)

    print(f"#{tc} {answer}")
