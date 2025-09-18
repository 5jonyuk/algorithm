sentenses = []

while True:
    sentense = input()
    if sentense == '.':
        break
    sentenses.append(sentense)

for sentense in sentenses:
    flag = False
    stack = []
    for word in sentense:
        if (word == '(' or word == '['):
            stack.append(word)

        elif (word == ')'):
            if (not stack or stack[-1] != '('):
                flag = True
                break
            else:
                stack.pop()

        elif (word == ']'):
            if (not stack or stack[-1] != '['):
                flag = True
                break
            else:
                stack.pop()
        else:
            continue

    if (not stack and flag == False):
        print('yes')
    else:
        print('no')
