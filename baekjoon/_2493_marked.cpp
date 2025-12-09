#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int &x : arr)
        cin >> x;

    stack<pair<int, int>> s;
    string ans;

    for (int i = 0; i < n; i++) {
        int h = arr[i];

        while (!s.empty() && s.top().first < h) {
            s.pop();
        }

        if (!s.empty()) {
            ans += to_string(s.top().second) + " ";
        } else {
            ans += "0 ";
        }

        s.push({h, i + 1});
    }

    cout << ans;
}