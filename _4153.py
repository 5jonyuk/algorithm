# a=[]
# b=[]
# c=[]

# while True:
#     x, y, z = map(int, input().split())

#     a.append(x)
#     b.append(y)
#     c.append(z)

#     if x == 0 and y == 0 and z == 0:
#         break

# for i in range(len(a)):
#     if a[i] == 0 and b[i] == 0 and c[i] == 0:
#         break
#     if a[i]**2 + b[i]**2 == c[i]**2 or a[i]**2 + c[i]**2 == b[i]**2 or b[i]**2 + c[i]**2 == a[i]**2:
#         print("right")
#     else:
#         print("wrong")

while (True):
    a = list(map(int, input().split()))
    a.sort()
    if (a == [0, 0, 0]):
        break
    if (a[0]**2+a[1]**2 == a[2]**2):
        print("right")
    else:
        print("wrong")
