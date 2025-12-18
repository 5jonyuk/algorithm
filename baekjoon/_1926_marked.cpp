#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// 벡터는 값을 참조하지 않고 복사하여 원본을 사용하려면 꼭 참조 표시를 꼭 해줘야함
int bfs(int x, int y, vector<vector<bool>> &visited, vector<vector<int>> &graph, int n, int m) {
    queue<pair<int, int>> Q;
    Q.push({x, y});
    visited[x][y] = true;
    int area = 0;

    while (!Q.empty()) {
        pair<int, int> cur = Q.front();
        Q.pop();
        area++;

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = dx[i] + cur.X;
            ny = dy[i] + cur.Y;

            if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (!visited[nx][ny] && graph[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    Q.push({nx, ny});
                }
            }
        }
    }

    return area;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> graph[i][j];
        }
    }
    vector<vector<bool>> visited(n, vector<bool>(m, false));

    int max_area = 0;
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[i][j] && graph[i][j] == 1) {
                int area;
                area = bfs(i, j, visited, graph, n, m);
                max_area = max(area, max_area);
                cnt++;
            }
        }
    }
    cout << cnt << "\n" << max_area;
}