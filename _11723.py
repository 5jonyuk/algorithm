import sys
input = sys.stdin.readline

m = int(input())

s_set = set()


def add(x):
    if (check(x) == 0):
        s_set.add(x)


def remove(x):
    if (check(x)):
        s_set.remove(x)


def check(x):
    if (x in s_set):
        return 1
    else:
        return 0


def toggle(x):
    if (check(x)):
        remove(x)
    else:
        add(x)


def all():
    global s_set
    s_set = set(range(1, 21))


def empty():
    global s_set
    s_set.clear()


for _ in range(m):
    op = input().strip().split()

    if (op[0] == 'add'):
        add(int(op[1]))
    elif (op[0] == 'remove'):
        remove(int(op[1]))
    elif (op[0] == 'check'):
        if (check(int(op[1]))):
            print(1)
        else:
            print(0)
    elif (op[0] == 'toggle'):
        toggle(int(op[1]))
    elif (op[0] == 'all'):
        all()
    else:
        empty()
