#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    int dx[3] = {1, -1, 2};

    queue<pair<int, int>> Q;
    bool visited[100001];
    fill(visited, visited + 100001, false);

    Q.push({n, 0});
    visited[n] = true;

    while (!Q.empty()) {
        auto cur = Q.front();
        Q.pop();

        if (cur.X == k) {
            cout << cur.Y;
            return 0;
        }

        for (int i = 0; i < 3; i++) {
            int nxt;
            if (i == 2) {
                nxt = cur.X * dx[i];
            } else {
                nxt = cur.X + dx[i];
            }

            if (nxt >= 0 && nxt < 100001 && !visited[nxt]) {
                visited[nxt] = true;
                Q.push({nxt, cur.Y + 1});
            }
        }
    }
}