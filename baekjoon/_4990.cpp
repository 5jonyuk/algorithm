#include <bits/stdc++.h>
using namespace std;

char arr[532001];

void solve(int x, int size) {
    if (size == 1) {
        arr[x] = '-';
        return;
    }

    size /= 3;

    for (int i = 0; i < 3; i++) {
        if (i == 1) {
            continue;
        }
        solve(x + i * size, size);
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    while (cin >> n) {
        if (n == 0) {
            cout << '-' << "\n";
            continue;
        }

        int len = 1;
        for (int i = 0; i < n; i++) {
            len *= 3;
        }

        fill(arr, arr + len, ' ');
        solve(0, len);

        for (int i = 0; i < len; i++) {
            cout << arr[i];
        }
        cout << "\n";
    }
}