#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int m, n, k;
int tc;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(pair<int, int> cabbage, vector<vector<int>> &ground, vector<vector<int>> &visited) {
    queue<pair<int, int>> q;
    q.push(cabbage);
    visited[cabbage.X][cabbage.Y] = 1;

    while (!q.empty()) {
        auto val = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = val.X + dx[i];
            ny = val.Y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (visited[nx][ny] == 0 && ground[nx][ny] == 1) {
                    visited[nx][ny] = 1;
                    q.push({nx, ny});
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> tc;

    for (int t = 0; t < tc; t++) {
        cin >> m >> n >> k;

        vector<vector<int>> ground(n, vector<int>(m));
        vector<vector<int>> visited(n, vector<int>(m));

        for (int i = 0; i < k; i++) {
            int x, y;
            cin >> x >> y;
            ground[y][x] = 1;
        }

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (ground[i][j] == 1 && visited[i][j] == 0) {
                    bfs({i, j}, ground, visited);
                    cnt++;
                }
            }
        }
        cout << cnt << "\n";
    }
}