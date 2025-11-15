def factorial(num):
    result = 1
    for i in range(2, num+1):
        result = result*i
    return result


n = int(input())
print(factorial(n))
