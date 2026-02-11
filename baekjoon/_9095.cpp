#include <bits/stdc++.h>
using namespace std;

int tc;
int dp[11];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> tc;

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 0; i < tc; i++) {
        int n;
        cin >> n;

        if (n < 4) {
            cout << dp[n] << "\n";
            continue;
        }

        for (int j = 4; j <= n; j++) {
            dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
        }

        cout << dp[n] << "\n";
    }
}