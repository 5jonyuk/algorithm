#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int m, n, k;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void dfs(int start_x, int start_y, vector<vector<int>> &arr, vector<vector<bool>> &visited) {
    stack<pair<int, int>> S;
    S.push({start_x, start_y});
    visited[start_x][start_y] = true;

    while (!S.empty()) {
        auto cur = S.top();
        S.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = cur.X + dx[i];
            ny = cur.Y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (visited[nx][ny] == false && arr[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    S.push({nx, ny});
                }
            }
        }
    }
    return;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {

        cin >> m >> n >> k;

        vector<vector<int>> arr(n, vector<int>(m, 0));
        vector<vector<bool>> visited(n, vector<bool>(m, false));

        for (int i = 0; i < k; i++) {
            int x, y;
            cin >> x >> y;

            arr[y][x] = 1;
        }

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] == false && arr[i][j] == 1) {
                    dfs(i, j, arr, visited);
                    cnt++;
                }
            }
        }
        cout << cnt << "\n";
    }
}