from collections import deque
n, k = map(int, input().split())
cntList = []


def bfs(start):
    visited = [False] * 100001
    distance = [0] * 100001
    visited[start] = True
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if (current == k):
            return distance[current]

        neighbors = [current+1, current-1, current*2]
        for neighbor in neighbors:
            if (0 <= neighbor < 100001 and visited[neighbor] == False):
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)


print(bfs(n))
