#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> v(3);

    for (int &x : v)
        cin >> x;

    sort(v.begin(), v.end());

    int same_nun = 0;
    int cnt = 1;

    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (v[i] != v[j])
                continue;
            same_nun = v[i];
            cnt++;
        }
    }
    if (cnt == 1) {
        auto max = max_element(v.begin(), v.end());
        cout << 100 * (*max);
    } else if (cnt == 2) {
        cout << 1000 + (same_nun * 100);
    } else {
        cout << 10000 + (same_nun * 1000);
    }
}