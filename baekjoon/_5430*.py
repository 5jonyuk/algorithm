# from collections import deque
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     errorFlag = False
#     p = deque(map(str, input().strip()))
#     n = int(input())
#     s = input().strip()
#     s = s.strip('[]')
#     if (n > 0):
#         arr = deque(map(int, s.split(',')))
#     else:
#         arr = deque(map(int, s))
#     flag = False
#     for i in range(len(p)):
#         if (p[i] == 'R' and flag == False):
#             flag = True
#         elif (p[i] == 'R' and flag == True):
#             flag = False
#         else:
#             if (len(arr) == 0):
#                 print('error')
#                 errorFlag = True
#                 break
#             else:
#                 if (flag == True):
#                     arr.pop()
#                 else:
#                     arr.popleft()
#     if (errorFlag):
#         continue

#     if (flag):
#         print('['+','.join(map(str, reversed(arr)))+']')
#     else:
#         print('['+','.join(map(str, arr))+']')

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().strip()
    n = int(input())
    s = input().strip()
    s = s.strip('[]')
    if (n > 0):
        arr = deque(map(int, s.split(',')))
    else:
        arr = deque()

    reverse = False
    errorFlag = False

    for cmd in p:
        if (cmd == 'R'):
            reverse = not reverse
        else:
            if (len(arr) == 0):
                print("error")
                errorFlag = True
                break
            else:
                if (reverse):
                    arr.pop()
                else:
                    arr.popleft()

    if (errorFlag):
        continue

    if (reverse):
        arr.reverse()

    print(f"[{','.join(map(str, arr))}]")
