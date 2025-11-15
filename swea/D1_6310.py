import random

a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

result = []
# for i in range(8):
#     randValue = random.randint(0, len(a) - 1)
#     result.append(a[randValue])
#
# print("".join(result))

for i in range(8):
    result.append(random.choice(a))

print("".join(result))

# 정답은 하드코딩으로...