#include <bits/stdc++.h>
using namespace std;

int n;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    vector<vector<int>> meet(n, vector<int>(2));

    for (int i = 0; i < n; i++) {
        int start, end;
        cin >> start >> end;

        meet[i] = {start, end};
    }

    sort(meet.begin(), meet.end(), [](vector<int> &a, vector<int> &b) {
        if (a[1] == b[1]) {
            return a[0] < b[0];
        }
        return a[1] < b[1];
    });

    int meet_end = meet[0][1];
    int cnt = 1;
    for (int i = 1; i < n; i++) {
        if (meet_end <= meet[i][0]) {
            meet_end = meet[i][1];
            cnt++;
        }
    }
    cout << cnt;
}