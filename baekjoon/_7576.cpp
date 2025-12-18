#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int m, n;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> m >> n;

    vector<vector<int>> graph(n, vector<int>(m));
    vector<vector<int>> visited(n, vector<int>(m, 0));
    queue<pair<int, int>> Q;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> graph[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 1) {
                Q.push({i, j}); // 동시확산을 구현하기 위해 익은 토마토들을 먼저 큐에 다 저장
            }
        }
    }

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = dx[i] + cur.X;
            ny = dy[i] + cur.Y;

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (visited[nx][ny] == 0 && graph[nx][ny] == 0) {
                    visited[nx][ny] = visited[cur.X][cur.Y] + 1;
                    graph[nx][ny] = 1;
                    Q.push({nx, ny});
                }
            }
        }
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 0) {
                cout << -1;
                return 0;
            }
            result = max(result, visited[i][j]);
        }
    }
    cout << result;
}