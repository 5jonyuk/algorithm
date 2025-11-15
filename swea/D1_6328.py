def compare(a, b):
    if (len(a) > len(b)):
        print(a)
    else:
        print(b)


a, b = map(str, input().split(', '))
compare(a, b)
