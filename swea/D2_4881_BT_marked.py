'''
백트래킹 
1. 현재 행과 여태까지 더한 값을 넘겨줌
2. 마지막 행까지 가면 최솟값을 저장
3. 가지치기: 더해지는 값이 답이나온 값보다 크면 가지치기
'''


def backtrack(row, total):
    global answer

    if row == n:
        answer = min(total, answer)

    if total >= answer:
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = True
            backtrack(row+1, total+matrix[row][col])
            visited[col] = False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    answer = int(1e9)
    backtrack(0, 0)
    print(f"#{tc} {answer}")
