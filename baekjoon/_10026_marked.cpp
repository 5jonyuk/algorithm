#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int n;
char arr[100][100];
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int start_x, int start_y, vector<vector<bool>> &visited, bool normal) {
    queue<pair<int, int>> Q;
    Q.push({start_x, start_y});
    visited[start_x][start_y] = true;

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = dx[i] + cur.X;
            ny = dy[i] + cur.Y;

            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                if (normal) {
                    if (!visited[nx][ny] && arr[nx][ny] == arr[cur.X][cur.Y]) {
                        visited[nx][ny] = true;
                        Q.push({nx, ny});
                    }
                } else {
                    if (!visited[nx][ny]) {
                        if (arr[nx][ny] == arr[cur.X][cur.Y] || (arr[nx][ny] == 'R' && arr[cur.X][cur.Y] == 'G') ||
                            (arr[nx][ny] == 'G' && arr[cur.X][cur.Y] == 'R')) {
                            visited[nx][ny] = true;
                            Q.push({nx, ny});
                        }
                    }
                }
            }
        }
    }
    return;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            arr[i][j] = s[j];
        }
    }

    bool normal = true;

    for (int k = 0; k < 2; k++) {
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    bfs(i, j, visited, normal);
                    cnt++;
                }
            }
        }
        cout << cnt << " ";
        normal = false;
    }
}