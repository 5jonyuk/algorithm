T = int(input())
for tc in range(1, T + 1):
    inputStr = input().split()
    stack = []
    error = False
    for s in inputStr:
        if s.isdigit():
            stack.append(int(s))
        elif s == ".":
            if len(stack) == 1:
                print(f"#{tc} {stack[0]}")
            else:
                print(f"#{tc} error")
            break
        else:
            if len(stack) < 2:
                print(f"#{tc} error")
                break
            a = stack.pop()
            b = stack.pop()

            if s == "+":
                stack.append(b + a)
            elif s == "-":
                stack.append(b - a)
            elif s == "*":
                stack.append(b * a)
            elif s == "/":
                stack.append(b // a)
            else:
                print(f"#{tc} error")
                break
