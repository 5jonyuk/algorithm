#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int n, m;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int graph[101][101];
int visited[101][101];

void bfs() {
    queue<pair<int, int>> Q;
    visited[0][0] = 1;
    Q.push({0, 0});

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = cur.X + dx[i];
            ny = cur.Y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                if (visited[nx][ny] == 0 && graph[nx][ny] == 1) {
                    visited[nx][ny] = visited[cur.X][cur.Y] + 1;
                    Q.push({nx, ny});
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            graph[i][j] = s[j] - '0';
            visited[i][j] = 0;
        }
    }

    bfs();
    cout << visited[n - 1][m - 1];
}

// int bfs(vector<vector<int>> &graph, int start_x, int start_y) {
//     queue<pair<int, int>> Q;
//     vector<vector<int>> visited(n, vector<int>(m, 0));
//     visited[start_x][start_y] = 1;
//     Q.push({start_x, start_y});

//     while (!Q.empty()) {
//         auto cur = Q.front();
//         Q.pop();

//         for (int i = 0; i < 4; i++) {
//             int nx, ny;
//             nx = dx[i] + cur.X;
//             ny = dy[i] + cur.Y;

//             if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
//                 if (visited[nx][ny] == 0 && graph[nx][ny] == 1) {
//                     visited[nx][ny] = visited[cur.X][cur.Y] + 1;
//                     Q.push({nx, ny});
//                 }
//             }
//         }
//     }
//     return visited[n - 1][m - 1];
// }

// int main() {
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     cin >> n >> m;

//     vector<vector<int>> graph(n, vector<int>(m));
//     for (int i = 0; i < n; i++) {
//         string s;
//         cin >> s;
//         for (int j = 0; j < m; j++) {
//             graph[i][j] = s[j] - '0';
//         }
//     }

//     cout << bfs(graph, 0, 0);
// }
