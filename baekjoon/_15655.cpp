#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[10];
int ans[10];

void backtrack(int idx, int start) {
    if (idx == m) {
        for (int i = 0; i < m; i++) {
            cout << ans[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = start; i < n; i++) {
        ans[idx] = arr[i];
        backtrack(idx + 1, i + 1);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + n);
    backtrack(0, 0);
}