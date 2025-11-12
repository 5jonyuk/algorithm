n = int(input())

number = [0]*10

while (n != 0):
    n_remainder = n % 10
    number[n_remainder] += 1
    n = n // 10

for i in range(10):
    print(i, end=" ")
print()
for i in range(10):
    print(number[i], end=" ")
