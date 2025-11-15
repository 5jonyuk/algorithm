num1 = [4, 29, 18, 13, 19, 25, 9, 6, 10, 24]
num2 = [18, 6, 23, 10, 27, 16, 11, 29, 13, 28, 9, 3, 15, 22, 19]

print(num1)
print(num2)

num3 = sorted(list(set(num1) & set(num2)))
print(num3)
