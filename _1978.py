N = int(input())
if (N <= 100):
    count = 0
    numberList = list(map(int, input().split()))
    if (len(numberList) != N):
        print("error")

    for number in numberList:
        if (number == 1):
            continue
        for i in range(2, number):
            if (number % i == 0):
                break
        else:  # for...else문 루프가 break를 만나지 않고 정상적으로 종료되었을 때 실행
            count += 1

print(count)
