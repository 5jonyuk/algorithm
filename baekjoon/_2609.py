x, y = map(int, input().split())

x_divisors=[]
y_divisors=[]
CD=[]

for i in range(1, x+1):
    if (x % i == 0):
        x_divisors.append(i)
for i in range(1, y+1):
    if (y % i == 0):
        y_divisors.append(i)

for x in x_divisors:
    for y in y_divisors:
        if x==y:CD.append(x)

GCD = max(CD)
print(GCD)

LCD = (x*y) // GCD
print(LCD)