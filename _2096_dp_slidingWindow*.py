import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())
prev = [(a, a),
        (b, b),
        (c, c)]

if (n > 1):
    for i in range(1, n):
        a, b, c = map(int, input().split())
        curr = [(0, 0)] * 3
        curr[0] = (a + max(prev[0][0], prev[1][0]),
                   a + min(prev[0][1], prev[1][1]))
        curr[1] = (b + max(prev[0][0], prev[1][0], prev[2][0]),
                   b + min(prev[0][1], prev[1][1], prev[2][1]))
        curr[2] = (c + max(prev[1][0], prev[2][0]),
                   c + min(prev[1][1], prev[2][1]))
        prev = curr

print(max(prev[0][0], prev[1][0], prev[2][0]),
      min(prev[0][1], prev[1][1], prev[2][1]))
