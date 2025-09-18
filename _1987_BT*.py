import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
visited = [False] * 26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def backtrack(x, y, cnt):
    global answer
    answer = max(answer, cnt)  # 방문할 때 마다 카운트 저장

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < r and 0 <= ny < c):
            idx = ord(board[nx][ny]) - ord('A')
            if (visited[idx] == False):  # 방문 처리가 안 된 알파벳을
                visited[idx] = True  # 방문 처리 후
                backtrack(nx, ny, cnt+1)  # 카운트를 1 올리고 다음 알파벳에서 다시 탐색
                visited[idx] = False  # 더 이상 탐색이 불가하다면 방문한 알파벳들 다 false처리


answer = 0
visited[ord(board[0][0])-ord('A')] = True  # ord(): 문자를 유니코드숫자로 변환
backtrack(0, 0, 1)
print(answer)
