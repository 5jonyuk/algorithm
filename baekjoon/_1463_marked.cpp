#include <bits/stdc++.h>
using namespace std;

int n;
int dp[1000001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    dp[1] = 0;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;
        if (i % 2 == 0) {
            dp[i] = min(dp[i], dp[i / 2] + 1);
        }
        if (i % 3 == 0) {
            dp[i] = min(dp[i], dp[i / 3] + 1);
        }
    }

    cout << dp[n];
}

/* bfs 방식 */

// #include <bits/stdc++.h>
// using namespace std;

// int n;
// int cnt;

// int bfs(int n) {
//     queue<int> q;
//     vector<int> dist(n + 1, -1);
//     q.push(n);
//     dist[n] = 0;

//     while (!q.empty()) {
//         int x = q.front();
//         q.pop();

//         if (x == 1) {
//             break;
//         }

//         if (dist[x - 1] == -1) {
//             q.push(x - 1);
//             dist[x - 1] = dist[x] + 1;
//         }
//         if (dist[x / 2] == -1 && x % 2 == 0) {
//             q.push(x / 2);
//             dist[x / 2] = dist[x] + 1;
//         }
//         if (dist[x / 3] == -1 && x % 3 == 0) {
//             q.push(x / 3);
//             dist[x / 3] = dist[x] + 1;
//         }
//     }
//     return dist[1];
// }

// int main() {
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     cin >> n;

//     cout << bfs(n);
// }