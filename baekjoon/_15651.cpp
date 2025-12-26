#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[10];
bool isUsed[10];

void backtrack(int idx) {
    if (idx == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= n; i++) {
        arr[idx] = i;
        backtrack(idx + 1);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    backtrack(0);
}