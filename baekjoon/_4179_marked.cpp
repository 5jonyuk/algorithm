#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    int r, c;
    cin >> r >> c;

    vector<vector<char>> miro(r, vector<char>(c));
    vector<vector<int>> jihunArr(r, vector<int>(c, -1));
    vector<vector<int>> fireArr(r, vector<int>(c, -1));

    queue<pair<int, int>> jihunQ;
    queue<pair<int, int>> fireQ;

    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < c; j++) {
            miro[i][j] = s[j];
            if (miro[i][j] == 'J') {
                jihunQ.push({i, j});
                jihunArr[i][j] = 0;
            } else if (miro[i][j] == 'F') {
                fireQ.push({i, j});
                fireArr[i][j] = 0;
            }
        }
    }

    while (!fireQ.empty()) {
        auto cur = fireQ.front();
        fireQ.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = dx[i] + cur.X;
            ny = dy[i] + cur.Y;

            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                if (miro[nx][ny] != '#' && fireArr[nx][ny] == -1) {
                    fireArr[nx][ny] = fireArr[cur.X][cur.Y] + 1;
                    fireQ.push({nx, ny});
                }
            }
        }
    }

    while (!jihunQ.empty()) {
        auto cur = jihunQ.front();
        jihunQ.pop();

        for (int i = 0; i < 4; i++) {
            int nx, ny;
            nx = dx[i] + cur.X;
            ny = dy[i] + cur.Y;

            if (nx >= 0 && nx < r && ny >= 0 && ny < c) {
                if (miro[nx][ny] != '#' && jihunArr[nx][ny] == -1) {
                    if (jihunArr[cur.X][cur.Y] + 1 < fireArr[nx][ny] || fireArr[nx][ny] == -1) {
                        jihunArr[nx][ny] = jihunArr[cur.X][cur.Y] + 1;
                        jihunQ.push({nx, ny});
                    }
                }
            } else {
                cout << jihunArr[cur.X][cur.Y] + 1;
                return 0;
            }
        }
    }
    cout << "IMPOSSIBLE";
}