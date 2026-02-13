#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<vector<int>> item(n, vector<int>(2));

    for (int i = 0; i < n; i++) {
        cin >> item[i][0] >> item[i][1];
    }

    sort(item.begin(), item.end());

    vector<vector<int>> dp(n + 1, vector<int>(k + 1));
    for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < k + 1; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
                continue;
            }
            if (item[i - 1][0] <= j) {
                dp[i][j] = max(dp[i - 1][j], item[i - 1][1] + dp[i - 1][j - item[i - 1][0]]);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << dp[n][k];
}