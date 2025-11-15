def calculateSquare(a, b):
    a_square = a*a
    b_square = b**2

    print(f"square({a}) => {a_square}")
    print(f"square({b}) => {b_square}")


a, b = map(int, input().split(","))
calculateSquare(a, b)
