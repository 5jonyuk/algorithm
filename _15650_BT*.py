n, m = map(int, input().split())
result = []


def backtrack(start):
    if (len(result) == m):
        print(*result)
        return

    for i in range(start, n+1):  # start로 무효후보를 애초에 제한하여 가지치기
        result.append(i)
        backtrack(i)
        result.pop() # 분기 탐색 후 돌아오는 백트래킹 과정


backtrack(1)
