#include <bits/stdc++.h>
using namespace std;

int n;
int dp[1000001];
int pre[1000001]; // 지나온 경로를 저장, 인덱스에 대한 최적의 경로를 값에 저장

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    dp[1] = 0;
    pre[1] = 0;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;
        pre[i] = i - 1;

        if (i % 2 == 0) {
            if (dp[i] > dp[i / 2] + 1) {
                pre[i] = i / 2;
            }
            dp[i] = min(dp[i], dp[i / 2] + 1);
        }
        if (i % 3 == 0) {
            if (dp[i] > dp[i / 3] + 1) {
                pre[i] = i / 3;
            }
            dp[i] = min(dp[i], dp[i / 3] + 1);
        }
    }

    cout << dp[n] << "\n";

    int i = n;
    while (i != 0) {
        cout << i << " ";
        i = pre[i];
    }
}