N, M = map(int, input().split())
cardNum = list(map(int, input().split()))
numMax = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cardNum[i]+cardNum[j]+cardNum[k]
            if (total <= M):
                numMax = max(numMax, total)

print(numMax)

# from itertools import combinations

# for combo in combinations(cardNum, 3): //cardNum List에서 3개씩 묶는 모든 조합을 combo에 담음
#     total = sum(combo)
#     if(total<=M):
#         numMax = max(numMax,total)
# print(numMax)
