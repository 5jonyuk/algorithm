#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<vector<int>> arr(7, vector<int>(2));

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;

        arr[b][a]++;
    }

    int answer = 0;
    for (int i = 1; i < 7; i++) {
        for (int j = 0; j < 2; j++) {
            answer += (arr[i][j] + k - 1) / k;
        }
    }
    cout << answer;
}