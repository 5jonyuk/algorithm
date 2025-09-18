import sys
input = sys.stdin.readline
n = int(input())

queue = []


def push(item):
    queue.append(item)


def pop():
    if (empty()):
        print(-1)
    else:
        num = queue.pop(0)
        print(num)


def front():
    if (empty()):
        print(-1)
    else:
        print(queue[0])


def back():
    if (empty()):
        print(-1)
    else:
        print(queue[-1])


def size():
    print(len(queue))


def empty():
    if (not queue):
        return 1
    else:
        return 0


for i in range(n):
    op = input().strip().split()

    if (op[0] == 'push'):
        push(int(op[1]))
    elif (op[0] == 'front'):
        front()
    elif (op[0] == 'back'):
        back()
    elif (op[0] == 'size'):
        size()
    elif (op[0] == 'empty'):
        print(empty())
    else:
        pop()
