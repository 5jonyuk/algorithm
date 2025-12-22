#include <bits/stdc++.h>
using namespace std;

int video[100][100];

bool check(int x, int y, int s) {
    for (int i = x; i < x + s; i++) {
        for (int j = y; j < y + s; j++) {
            if (video[x][y] != video[i][j]) {
                return false;
            }
        }
    }
    return true;
}

void recursion(int x, int y, int size) {
    if (check(x, y, size)) {
        cout << video[x][y];
        return;
    }

    size /= 2;

    cout << "(";
    recursion(x, y, size);
    recursion(x, y + size, size);
    recursion(x + size, y, size);
    recursion(x + size, y + size, size);
    cout << ")";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        for (int j = 0; j < n; j++) {
            video[i][j] = s[j] - '0';
        }
    }

    recursion(0, 0, n);
}