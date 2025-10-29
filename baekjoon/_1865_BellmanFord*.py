'''
벨만포드
1. 에지 리스트로 그래프(edges=[(start, end, weight)])를 구현하고 최단 경로 리스트(distance) 초기화 하기
2. 모든 에지를 확인해 정답 리스트 업데이트하기
    2-1. 업데이트 조건 
        - distance[start] != INF 여야함 
            => 이 문제에서는 최단경로를 구하는 것이 아닌 단순히 음수사이클 탐지하고 시작점과 떨어진 곳에서 음수사이클이 발생할 수도 있기에 빼기!!
        - distance[end] > distance[start] + weigth 라면 distance[end] = distance[start] + weigth
    2-2. 업데이트 반복횟수는 노드개수-1 => 다 돌면 최단거리 나옴
    2-3. 각 업데이트 반복횟수의 의미는 반복횟수가 2번 이라면 2개의 에지를 사용했을 때 각 노드에 대한 최단거리
3. 음수 사이클을 확인하기 위해 반복을 한 번 더 해봄 
    3-1. 경로가 갱신이 되면 음수사이클(사이클의 합이 음수) 발생 => 최단거리가 -무한대가 됨
    3-2. 경로가 갱신되지 않는다면 음수사이클 없음
'''
import sys
input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start, n):
    distance = [INF]*(n+1)
    distance[start] = 0

    for i in range(n):
        for edge in edges:
            s, e, w = edge
            if (distance[e] > distance[s] + w):
                distance[e] = distance[s] + w
                if (i == n-1):
                    return True
    return False


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # 음수 사이클이 존재하면 어떤 정점에서든 그 사이클에 도달할 수 있는 경로가 존재하기 때문에 임의로 시작정점을 잡음
    negative_cycle = bellman_ford(1, n)

    if (negative_cycle):
        print("YES")
    else:
        print("NO")
