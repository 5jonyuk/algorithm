import sys
input = sys.stdin.readline
n = int(input())

stack = []


def push(item):
    stack.append(item)


def pop():
    global location
    if (empty()):
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if (not stack):
        return 1
    else:
        return 0


def top():
    if (empty()):
        return -1
    else:
        return stack[-1]


for _ in range(n):
    op = input().strip()
    opList = op.split()
    if (opList[0] == 'push'):
        push(opList[1])
    elif (opList[0] == 'pop'):
        print(pop())
    elif (opList[0] == 'size'):
        print(size())
    elif (opList[0] == 'empty'):
        print(empty())
    else:
        print(top())
