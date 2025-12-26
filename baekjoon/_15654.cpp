#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[8];
int ans[8];
int isUsed[10001];

void backtrack(int idx) {
    if (idx == m) {
        for (int i = 0; i < m; i++) {
            cout << ans[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 0; i < n; i++) {
        if (!isUsed[arr[i]]) {
            isUsed[arr[i]] = 1;
            ans[idx] = arr[i];
            backtrack(idx + 1);
            isUsed[arr[i]] = 0;
        }
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

    backtrack(0);
}