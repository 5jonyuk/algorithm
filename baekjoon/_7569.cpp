#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int n, m, h;
int arr[100][100][100];
int dx[6] = {-1, 1, 0, 0, 0, 0};
int dy[6] = {0, 0, -1, 1, 0, 0};
int dz[6] = {0, 0, 0, 0, -1, 1};
queue<pair<int, pair<int, int>>> Q;

int bfs() {
    int cnt = 0;
    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        for (int i = 0; i < 6; i++) {
            int nx, ny, nz;
            nx = dx[i] + cur.Y.X;
            ny = dy[i] + cur.Y.Y;
            nz = dz[i] + cur.X;

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && nz >= 0 && nz < h) {
                if (arr[nz][nx][ny] == 0) {
                    arr[nz][nx][ny] = arr[cur.X][cur.Y.X][cur.Y.Y] + 1;
                    cnt = max(arr[nz][nx][ny], cnt);
                    Q.push({nz, {nx, ny}});
                }
            }
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int result;

    cin >> m >> n >> h;

    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> arr[k][i][j];
                if (arr[k][i][j] == 1) {
                    Q.push({k, {i, j}});
                }
            }
        }
    }
    result = bfs();

    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[k][i][j] == 0) {
                    cout << -1;
                    return 0;
                }
            }
        }
    }

    if (result != 0) {
        result--;
    }

    cout << result;
}
