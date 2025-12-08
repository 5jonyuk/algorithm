#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> arr(n);
    for (int &x : arr) {
        cin >> x;
    }

    int v;
    cin >> v;

    // int cnt = 0;
    // for (int x : arr) {
    //     if (x == v) {
    //         cnt++;
    //     }
    // }
    // cout << cnt;

    cout << count(arr.begin(), arr.end(), v);
}