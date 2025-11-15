def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


n = int(input())
if is_prime(n):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
