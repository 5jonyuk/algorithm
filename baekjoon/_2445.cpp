#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i + 1; j++) {
            cout << "*";
        }
        for (int k = 2 * n; k > (i + 1) * 2; k--) {
            cout << " ";
        }
        for (int j = 0; j < i + 1; j++) {
            cout << "*";
        }
        cout << "\n";
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            cout << "*";
        }
        for (int k = 0; k < i * 2; k++) {
            cout << " ";
        }
        for (int j = 0; j < n - i; j++) {
            cout << "*";
        }
        cout << "\n";
    }
}