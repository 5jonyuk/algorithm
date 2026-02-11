#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        int num;
        cin >> num;
        arr[i] = num + arr[i - 1];
    }

    for (int tc = 0; tc < m; tc++) {
        int i, j;
        cin >> i >> j;
        cout << arr[j] - arr[i - 1] << "\n";
    }
}