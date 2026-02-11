#include <bits/stdc++.h>
using namespace std;

int n;
int stair[301];
int dp[301];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> stair[i];
    }

    if (n >= 1) {
        dp[1] = stair[1];
    }
    if (n >= 2) {
        dp[2] = stair[1] + stair[2];
    }
    if (n >= 3) {
        for (int i = 3; i <= n; i++) {
            dp[i] = max(stair[i] + stair[i - 1] + dp[i - 3], stair[i] + dp[i - 2]);
        }
    }

    cout << dp[n];
}