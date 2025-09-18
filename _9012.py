import sys
# sys.stdin.readline을 사용하면 끝에 '\n' 개행문자가 붙음 그래서 제거해줘야함
input = sys.stdin.readline

n = int(input())
lines = []

for _ in range(n):
    lines.append(input().strip())

for line in lines:
    stack = []
    flag = True
    for word in line:
        if (word == '('):
            stack.append(word)
        else:
            if (not stack or stack[-1] != '('):
                flag = False
                break
            else:
                stack.pop()

    if (not stack and flag == True):
        print('YES')
    else:
        print('NO')
