#include <bits/stdc++.h>
using namespace std;

int paper[2200][2200];
int cnt[3];

bool check(int x, int y, int s) {
    for (int i = x; i < x + s; i++) {
        for (int j = y; j < y + s; j++) {
            if (paper[x][y] != paper[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void solve(int x, int y, int size) {
    if (check(x, y, size)) {
        cnt[paper[x][y] + 1] += 1;
        return;
    }

    size /= 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            solve(x + i * size, y + j * size, size);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> paper[i][j];
        }
    }

    solve(0, 0, n);

    for (int i = 0; i < 3; i++) {
        cout << cnt[i] << "\n";
    }
}