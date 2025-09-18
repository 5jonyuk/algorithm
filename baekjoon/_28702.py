x = input()
y = input()
z = input()


if (x.isdigit()):
    x_int = int(x)+3
    # %15먼저 해야함 why? %3을 먼저했을 때 15같은 값이 나오면 %3조건이 먼저 참이 되어 %15조건으로 못가기 때문
    if (x_int % 3 == 0 and x_int % 5 == 0):
        print('FizzBuzz')
    elif (x_int % 5 == 0):
        print('Buzz')
    elif (x_int % 3 == 0):
        print('Fizz')
    else:
        print(x_int)
elif (y.isdigit()):
    y_int = int(y)+2
    if (y_int % 3 == 0 and y_int % 5 == 0):
        print('FizzBuzz')
    elif (y_int % 5 == 0):
        print('Buzz')
    elif (y_int % 3 == 0):
        print('Fizz')
    else:
        print(y_int)
else:
    z_int = int(z)+1
    if (z_int % 3 == 0 and z_int % 5 == 0):
        print('FizzBuzz')
    elif (z_int % 5 == 0):
        print('Buzz')
    elif (z_int % 3 == 0):
        print('Fizz')
    else:
        print(z_int)
