#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tc;
    cin >> tc;

    int cnt = 0;

    while (tc--) {
        string s;
        cin >> s;

        stack<char> st;
        for (char c : s) {
            if (st.empty() || st.top() != c) {
                st.push(c);
            } else {
                st.pop();
            }
        }
        if (st.empty()) {
            cnt++;
        }
    }

    cout << cnt;
}