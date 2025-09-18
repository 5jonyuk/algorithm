from collections import deque
n = int(input())
m = int(input())

computer = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)


def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    cnt = 0

    while queue:
        currentComputer = queue.popleft()
        for neighborComputer in computer[currentComputer]:
            if (visited[neighborComputer] == False):
                visited[neighborComputer] = True
                queue.append(neighborComputer)
                cnt += 1
    return cnt


print(bfs(1))
