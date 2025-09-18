n = int(input())
queen = [0]*n
cnt = 0

'''
abs(row-r) == abs(queen[row]-queen[r])
대각선을 체크하기 위한 코드 

현재위치가 (3,3)이라 가정 했을 때 
왼쪽 대각선들의 좌표는 (2,2),(1,1),(0,0) 일 것임 이 때의 각각 x좌표와 y좌표를 빼면 그 둘의 값이 같은 것을 알 수 있음
오른쪽 대각선들의 좌표는 (2,4),(1,5),(0,6) 일 것임 이 때의 각각 x좌표와 y좌표를 빼면 (1,-1),(2,-2),(3,-3)이므로 절댓값을 취하면 그 둘의 값이 같은 것을 알 수 있음

따라서 abs(row-r) x좌표(행)의 값을 뺀 절댓값과 
abs(queen[row]-queen[r]) y좌표(열)의 값을 뺀 절댓값이 같으면 대각선을 체크하는 것임
'''


def check(row):
    for r in range(row):
        # 같은 열인지 또는 대각선에 위치하는지 체크
        if (queen[row] == queen[r] or abs(row-r) == abs(queen[row]-queen[r])):
            return False
    return True


def dfs(row):
    global cnt
    if (row == n):
        cnt += 1
        return

    for col in range(n):
        queen[row] = col
        if (check(row)):  # 백트래킹(가지치기)
            dfs(row+1)


dfs(0)
print(cnt)
