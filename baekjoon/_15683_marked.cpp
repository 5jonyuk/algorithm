#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
/*
변수들이 가질 수 있는 값이 여러가지이고 변수들의 조합을 다 확인해보고 싶은데
각 변수들끼리는 독립적이라면 백트래킹보단 진법을 사용하여 풀기
ex. 가능한 방향의 종류는 4종류이므로 4진법을 사용, cctv의 갯수가 3개이면 0 ~ 4^3-1 까지 구하기
*/

int n, m;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int originGraph[10][10];
int updateGraph[10][10];
vector<pair<int, int>> cctv;

void copyGraph() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            updateGraph[i][j] = originGraph[i][j];
        }
    }
}

bool OOB(int x, int y) { return x < 0 || x >= n || y < 0 || y >= m; }

void watch(int x, int y, int dir) {
    dir %= 4;

    while (1) {
        x += dx[dir];
        y += dy[dir];

        if (OOB(x, y) || updateGraph[x][y] == 6) {
            return;
        }

        if (updateGraph[x][y] != 0) {
            continue;
        }

        updateGraph[x][y] = 7;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    int blindSpotCnt = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> originGraph[i][j];
            if (originGraph[i][j] != 0 && originGraph[i][j] < 6) {
                cctv.push_back({i, j});
            }
            if (originGraph[i][j] == 0) {
                blindSpotCnt++;
            }
        }
    }

    // 왼쪽 쉬프트 계산은 2^n 인데 문제에서는 4^n을 구해야하니 2를 추가로 곱해
    // 2^(2*cctv.size()) -> (2^2)^cctv.size()로 표현
    // cctv가 가질 수 있는 모든 방향의 경우의 수를 거치게 됨
    for (int num = 0; num < (1 << (2 * cctv.size())); num++) {
        copyGraph();
        int tmp = num; // num은 4진수로 변환될 대상

        for (int i = 0; i < cctv.size(); i++) {
            int dir = tmp % 4;
            tmp /= 4;

            int x = cctv[i].X;
            int y = cctv[i].Y;

            if (originGraph[x][y] == 1) {
                watch(x, y, dir);
            } else if (originGraph[x][y] == 2) {
                watch(x, y, dir);
                watch(x, y, dir + 2);
            } else if (originGraph[x][y] == 3) {
                watch(x, y, dir);
                watch(x, y, dir + 1);
            } else if (originGraph[x][y] == 4) {
                watch(x, y, dir);
                watch(x, y, dir + 1);
                watch(x, y, dir + 2);
            } else {
                watch(x, y, dir);
                watch(x, y, dir + 1);
                watch(x, y, dir + 2);
                watch(x, y, dir + 3);
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (updateGraph[i][j] == 0) {
                    result++;
                }
            }
        }
        blindSpotCnt = min(blindSpotCnt, result);
    }
    cout << blindSpotCnt;
}
