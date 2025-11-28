#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 3; i++) {
        int a, b, c, d;

        cin >> a >> b >> c >> d;

        if (a + b + c + d == 0) {
            cout << "D" << "\n";
        } else if (a + b + c + d == 1) {
            cout << "C" << "\n";
        } else if (a + b + c + d == 2) {
            cout << "B" << "\n";
        } else if (a + b + c + d == 3) {
            cout << "A" << "\n";
        } else {
            cout << "E" << "\n";
        }
    }
}