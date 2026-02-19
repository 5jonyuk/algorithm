#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int m, n, h;
int dz[6] = {-1, 1, 0, 0, 0, 0};
int dx[6] = {0, 0, -1, 1, 0, 0};
int dy[6] = {0, 0, 0, 0, -1, 1};

queue<pair<int, pair<int, int>>> q;

void bfs(vector<vector<vector<int>>> &box) {
    while (!q.empty()) {
        auto cur = q.front();
        q.pop();

        for (int i = 0; i < 6; i++) {
            int nz, nx, ny;
            nz = cur.X + dz[i];
            nx = cur.Y.X + dx[i];
            ny = cur.Y.Y + dy[i];

            if (nz >= 0 && nz < h && nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (box[nz][nx][ny] == 0) {
                    box[nz][nx][ny] = box[cur.X][cur.Y.X][cur.Y.Y] + 1;
                    q.push({nz, {nx, ny}});
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> m >> n >> h;
    vector<vector<vector<int>>> box(h, vector<vector<int>>(n, vector<int>(m)));

    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> box[k][i][j];
                if (box[k][i][j] == 1) {
                    q.push({k, {i, j}});
                }
            }
        }
    }

    bfs(box);

    int result = 0;
    for (int k = 0; k < h; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (box[k][i][j] == 0) {
                    cout << -1;
                    return 0;
                }
                result = max(result, box[k][i][j]);
            }
        }
    }
    cout << result - 1;
}