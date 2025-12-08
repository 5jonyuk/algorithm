#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s1, s2;
        cin >> s1 >> s2;

        vector<int> freq(26);
        for (char c : s1) {
            freq[c - 'a']++;
        }

        for (char c : s2) {
            freq[c - 'a']--;
        }

        bool flag = true;
        for (int x : freq) {
            if (x != 0) {
                flag = false;
                break;
            }
        }
        cout << (flag ? "Possible" : "Impossible");

        cout << "\n";
    }
}