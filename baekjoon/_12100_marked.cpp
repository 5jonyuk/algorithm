#include <bits/stdc++.h>
using namespace std;

int n;
int board[21][21];
int updateBoard[21][21];

void copyBoard() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            updateBoard[i][j] = board[i][j];
        }
    }
}

void rotate() {
    int temp[21][21];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            temp[i][j] = updateBoard[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            updateBoard[i][j] = temp[n - 1 - j][i];
        }
    }
    // 행과 열이 같으므로 swap은 필요없음
}

void tilt(int dir) {
    /*
    방향별로 각각 기울이지 않고 보드판 자체를 시계방향으로 돌려서 왼쪽으로 기울이는 것만 구하기
    dir == 0 -> 0도
    dir == 1 -> 90도
    dir == 2 -> 180도
    dir == 3 -> 270도
    */

    while (dir--) {
        rotate();
    }

    for (int i = 0; i < n; i++) {
        int tilted[21] = {}; // 왼쪽으로 기울였을 때의 값을 담을 배열
        int idx = 0;         // tilted 배열에 값이 들어가야할 위치를 가리키는 인덱스
        for (int j = 0; j < n; j++) {
            if (updateBoard[i][j] == 0) { // 빈칸일 때
                continue;
            }
            if (tilted[idx] == 0) { // tilted 배열이 비어있을 때는 바로 맨 앞에 삽입
                tilted[idx] = updateBoard[i][j];
            } else if (tilted[idx] ==
                       updateBoard[i][j]) { // tilted 배열이 가리키고 있는 값이 현재 들어오는 값과 같을 경우
                tilted[idx++] *= 2;
            } else { // tilted 배열이 가리키고 있는 값이 현재 들어오는 값과 다를 경우
                tilted[++idx] = updateBoard[i][j];
            }
        }
        for (int j = 0; j < n; j++) { // 기울인 최종 결과를 보드에 덮어쓰기
            updateBoard[i][j] = tilted[j];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    int answer = 0;
    // 5번 이동을 해야하고 각각 기울일 수 있는 방향은 4가지이므로 경우의 수는 4^5(1024)
    for (int caseNum = 0; caseNum < 1024; caseNum++) {
        copyBoard();
        int temp = caseNum;
        for (int i = 0; i < 5; i++) {
            int dir = temp % 4;
            temp /= 4;
            tilt(dir);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer = max(answer, updateBoard[i][j]);
            }
        }
    }
    cout << answer;
}