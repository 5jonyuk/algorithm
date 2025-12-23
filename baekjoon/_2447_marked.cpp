#include <bits/stdc++.h>
using namespace std;

char arr[2200][2200];

void solve(int x, int y, int size) {
    if (size == 1) {
        arr[x][y] = '*';
        return;
    }
    size /= 3;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == 1 && j == 1) {
                continue;
            }
            solve(x + i * size, y + j * size, size);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    memset(arr, ' ', sizeof(arr));
    solve(0, 0, n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i][j];
        }
        cout << "\n";
    }
}