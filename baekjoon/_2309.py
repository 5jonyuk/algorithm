from itertools import combinations

nanjaeng2Arr = []
for _ in range(9):
    nanjaeng2Arr.append(int(input()))

sevenNanjaeng2 = list(combinations(nanjaeng2Arr, 7))

for team in sevenNanjaeng2:
    if sum(team) == 100:
        team = sorted(team)
        for t in team:
            print(t)
        break
