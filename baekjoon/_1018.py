row, col = map(int, input().split())
wcnt = 0
bcnt = 0
chessList = []
bCntList = []
wCntList = []


for i in range(row):
    chessList.append(input())

for i in range(row-8+1):
    for j in range(col-8+1):
        for r in range(8):
            for c in range(8):
                if (chessList[i+0][j+0] == 'B'):
                    if (r % 2 == 0):
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'B'):
                            wcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'W'):
                            wcnt += 1
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'W'):
                            bcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'B'):
                            bcnt += 1
                    else:
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'W'):
                            wcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'B'):
                            wcnt += 1
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'B'):
                            bcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'W'):
                            bcnt += 1

                if (chessList[i+0][j+0] == 'W'):
                    if (r % 2 == 0):
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'W'):
                            bcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'B'):
                            bcnt += 1
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'B'):
                            wcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'W'):
                            wcnt += 1
                    else:
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'B'):
                            bcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'W'):
                            bcnt += 1
                        if (c % 2 == 0 and chessList[i+r][j+c] == 'W'):
                            wcnt += 1
                        if (c % 2 != 0 and chessList[i+r][j+c] == 'B'):
                            wcnt += 1
        wCntList.append(wcnt)
        bCntList.append(bcnt)
        wcnt = 0
        bcnt = 0

minCnt = min(min(wCntList), min(bCntList))

print(minCnt)
