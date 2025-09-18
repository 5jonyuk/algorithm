from collections import deque
n = int(input())

cardDeque = deque(range(1, n+1))

# for i in range(1, n+1):
#     cardDeque.append(i)

i = 0
while len(cardDeque) > 1:
    if (i % 2 == 0):
        cardDeque.popleft()
    else:
        cardDeque.append(cardDeque.popleft())
    i += 1

print(cardDeque[0])
