import math
A, B, V = map(int, input().split())

# 반복문
# while (True):
#     day = day+A
#     if (day == V or day > V):
#         break

#     day = day-B
#     daycnt += 1

print(math.ceil((V-A)/(A-B))+1)

# V-A : 정상까지 올라가기 직전까지 올라가야 하는 양
# A-B : 하루에 올라가는 양
# +1 : 마지막날은 무조건 A만큼 가면 안 미끄러지므로 마지막날을 제외하고 구한 뒤(V-A) +1
