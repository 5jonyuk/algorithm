#include <bits/stdc++.h>
using namespace std;

int n;
int rgb[1001][3];
int dp[1001][3]; // 여태까지 칠해온 값 저장

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> rgb[i][j];
        }
    }

    dp[0][0] = rgb[0][0];
    dp[0][1] = rgb[0][1];
    dp[0][2] = rgb[0][2];

    for (int i = 1; i < n; i++) {
        // i번째 집을 빨강으로 칠하고 여태까지 칠해온 게 초록과 파랑중 작은 값
        dp[i][0] = rgb[i][0] + min(dp[i - 1][1], dp[i - 1][2]);

        // i번째 집을 초록으로 칠하고 여태까지 칠해온 게 빨강과 파랑중 작은 값
        dp[i][1] = rgb[i][1] + min(dp[i - 1][0], dp[i - 1][2]);

        // i번째 집을 파랑으로 칠하고 여태까지 칠해온 게 빨강과 초록중 작은 값
        dp[i][2] = rgb[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
    }

    cout << min(min(dp[n - 1][0], dp[n - 1][1]), dp[n - 1][2]);
}