#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> alpa(26);

    string S;
    cin >> S;

    for (char s : S) {
        int idx = int(s) % 97;
        alpa[idx]++;
    }

    for (int x : alpa)
        cout << x << " ";
}
