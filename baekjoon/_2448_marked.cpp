#include <bits/stdc++.h>
using namespace std;

char arr[3080][6150];

void solve(int x, int y, int size) {
    if (size == 3) {
        arr[x][y] = '*';
        arr[x + 1][y - 1] = arr[x + 1][y + 1] = '*';
        for (int i = -2; i < 3; i++) {
            arr[x + 2][y + i] = '*';
        }
        return;
    }
    size /= 2;

    solve(x, y, size);
    solve(x + size, y - size, size);
    solve(x + size, y + size, size);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;

    fill(&arr[0][0], &arr[0][0] + 3080 * 6150, ' ');
    solve(0, n - 1, n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2 * n; j++) {
            cout << arr[i][j];
        }
        cout << "\n";
    }
}