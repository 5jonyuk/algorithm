#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long s, e;
    cin >> s >> e;

    if (s > e) {
        swap(s, e);
    }
    if (s == e || s + 1 == e) {
        cout << 0;
        return 0;
    }
    cout << e - s - 1 << "\n";
    for (long long i = s + 1; i < e; i++) {
        cout << i << " ";
    }
}