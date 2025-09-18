import sys
input = sys.stdin.readline

S = input().strip()
bomb = input().strip()
bombLen = len(bomb)
stack = []

for ch in S:
    stack.append(ch)
    if (len(stack) >= bombLen and "".join(stack[-bombLen:]) == bomb):
        del stack[-bombLen:]

if (not stack):
    print("FRULA")
else:
    print("".join(map(str, stack)))
