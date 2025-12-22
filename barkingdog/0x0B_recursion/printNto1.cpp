#include <bits/stdc++.h>
using namespace std;

void print(int n) {
    if (n > 0) {
        cout << n << " ";
        print(n - 1);
    }
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    print(n);
}