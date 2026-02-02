#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int r, c;

int graphPaper[11][11];
int laptop[41][41];

bool pasteable(int x, int y) {
    // 현재 노트북의 위치에서 스티커를 붙일 수 있는지 확인
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (laptop[x + i][y + j] == 1 && graphPaper[i][j] == 1) {
                return false;
            }
        }
    }

    // 확인 후 스티커 붙이기
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (graphPaper[i][j] == 1) {
                laptop[x + i][y + j] = 1;
            }
        }
    }

    return true;
}

// 90도 회전 함수
void rotate() {
    int temp[12][12];

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            temp[i][j] = graphPaper[i][j];
        }
    }

    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            // 회전 후의 값(graphPaper[i][j])에는
            // 회전 전의 값(temp[r - 1 - j][i])이 들어간다
            graphPaper[i][j] = temp[r - 1 - j][i];
        }
    }

    swap(r, c);
}

int main() {
    cin >> n >> m >> k;

    while (k--) {
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> graphPaper[i][j];
            }
        }

        // 0도, 90도, 180도, 270도 4번을 돌기 때문
        for (int rot = 0; rot < 4; rot++) {
            bool isPaste = false;
            for (int x = 0; x <= n - r; x++) {
                for (int y = 0; y <= m - c; y++) {
                    if (pasteable(x, y)) { // 현재 노트북의 위치를 전달
                        isPaste = true;
                        break;
                    }
                }
                if (isPaste) {
                    break;
                }
            }
            if (isPaste) {
                break;
            }
            rotate();
        }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (laptop[i][j] == 1) {
                answer++;
            }
        }
    }
    cout << answer;
}