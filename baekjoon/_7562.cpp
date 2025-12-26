#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int dx[8] = {-1, -2, -1, -2, 1, 2, 1, 2};
int dy[8] = {-2, -1, 2, 1, -2, -1, 2, 1};

int bfs(int start_x, int start_y, int target_x, int target_y, int size) {
    queue<pair<int, int>> Q;
    vector<vector<int>> visited(size, vector<int>(size, 0));
    Q.push({start_x, start_y});

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        if (cur.X == target_x && cur.Y == target_y) {
            return visited[cur.X][cur.Y];
        }

        for (int i = 0; i < 8; i++) {
            int nx, ny;
            nx = dx[i] + cur.X;
            ny = dy[i] + cur.Y;

            if (nx >= 0 && nx < size && ny >= 0 && ny < size) {
                if (visited[nx][ny] == 0) {
                    visited[nx][ny] = visited[cur.X][cur.Y] + 1;
                    Q.push({nx, ny});
                }
            }
        }
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tc;
    cin >> tc;

    for (int i = 0; i < tc; i++) {
        int I;
        int start_x, target_x;
        int start_y, target_y;

        cin >> I;
        cin >> start_x >> start_y;
        cin >> target_x >> target_y;

        if (start_x == target_x && start_y == target_y) {
            cout << 0 << "\n";
            continue;
        }

        cout << bfs(start_x, start_y, target_x, target_y, I) << "\n";
    }
}