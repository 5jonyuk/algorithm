alpabet_dict = {chr(96+i): i for i in range(1, 27)}
r = 31
M = 1234567891
hashValue = 0

L = int(input())
englishStr = list(input())

for i in range(0, L):
    hashValue += alpabet_dict[englishStr[i]]*pow(r, i)
    hashValue = hashValue % M

print(hashValue)
