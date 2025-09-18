import sys
input = sys.stdin.readline
n, m = map(int, input().split())

site = {}
for _ in range(n):
    siteUrl, pw = map(str, input().strip().split())
    site[siteUrl] = pw
for _ in range(m):
    question = input().strip()
    print(site[question])
