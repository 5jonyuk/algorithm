#include <bits/stdc++.h>
using namespace std;

int arr[1025][1025];

int solve(int x, int y, int size) {
    if (size == 1) {
        return arr[x][y];
    }
    size /= 2;

    int a = solve(x, y, size);
    int b = solve(x, y + size, size);
    int c = solve(x + size, y, size);
    int d = solve(x + size, y + size, size);

    vector<int> v = {a, b, c, d};
    sort(v.begin(), v.end(), greater<int>()); // 내림차순 정렬

    return v[1];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    cout << solve(0, 0, n);
}