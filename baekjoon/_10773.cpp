#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int k;
    cin >> k;

    stack<int> S;

    while (k--) {
        int n;
        cin >> n;

        if (n != 0) {
            S.push(n);
        } else {
            S.pop();
        }
    }

    int result = 0;
    int size = S.size();
    for (int i = 0; i < size; i++) {
        result += S.top();
        S.pop();
    }
    cout << result;
}