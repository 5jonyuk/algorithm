/*
D[4] = ?
1+1+1+1, 3+1, 2+1+1, 1+2+1 -> (3을 1,2,3의 합으로 나타내는 방법) + 1
1+1+2, 2+2 -> (2을 1,2의 합으로 나타내는 방법) + 2
1+3 -> (1을 1,2,3의 합으로 나타내는 방법) + 3

=> D[4] = D[1] + D[2] + D[3]
*/
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