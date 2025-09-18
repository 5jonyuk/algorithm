# 50점
n = int(input())
m = int(input())
s = input()
# cnt = 0
# ans = "I"
# for i in range(n):
#     ans += "OI"

# for i in range(m):
#     if (s[i] == "I"):
#         if (s[i:i+len(ans)] == ans):
#             cnt += 1

# print(cnt)

cur = 0
cnt = 0
ans = 0

while (cur < m-1):
    if (s[cur:cur+3] == "IOI"):
        cur += 2
        cnt += 1
        if (cnt == n):
            ans += 1
            cnt -= 1
    else:
        cur += 1
        cnt = 0
print(ans)
