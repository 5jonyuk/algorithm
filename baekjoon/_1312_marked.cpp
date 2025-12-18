#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, n;

    cin >> a >> b >> n;
    int value = a % b;

    int result = 0;
    while (n--) {
        value = value * 10;
        result = value / b;
        value = value % b;
    }
    cout << result;
}