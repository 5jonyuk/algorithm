#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        vector<bool> visited(26, false);

        string s;
        cin >> s;

        visited[s[0] - 'a'] = true;
        bool flag = true;

        for (int j = 1; j < s.length(); j++) {
            int idx = s[j] - 'a';
            if (s[j] != s[j - 1]) {
                if (visited[idx] == true) {
                    flag = false;
                    break;
                } else {
                    visited[idx] = true;
                }
            }
        }

        if (flag) {
            cnt++;
        }
    }

    cout << cnt;
}