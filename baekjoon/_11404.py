'''
1. 노드들의 관계를 표현할 그래프 무한대로 초기화
2. 자기 자신으로 가는 간선들은 0 으로 초기화
3. 주어진 정보 입력
4. 최단거리 계산(플로이드-워셜) 점화식: d[i][j] = min(d[i][j], d[i][k]+d[k][j])
5. 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 1.
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 2.
for i in range(1, n+1):
    for j in range(1, n+1):
        if (i == j):
            graph[i][j] = 0

# 3.
for _ in range(m):
    a, b, c = map(int, input().split())
    if (graph[a][b] > c):
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i == j):
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if (graph[i][j] == INF):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
