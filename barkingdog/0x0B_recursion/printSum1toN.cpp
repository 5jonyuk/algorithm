#include <bits/stdc++.h>
using namespace std;

int sum(int n) {
    if (n > 0) {
        return n + sum(n - 1);
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    cout << sum(n);
}