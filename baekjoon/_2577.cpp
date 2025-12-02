#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> freq(10);

    int a, b, c;
    cin >> a >> b >> c;

    int total = a * b * c;

    while (total > 0) {
        freq[total % 10]++;
        total /= 10;
    }
    for (int f : freq) {
        cout << f << "\n";
    }
}