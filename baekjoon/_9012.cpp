#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int tc;
    cin >> tc;

    while (tc--) {
        string ps;
        cin >> ps;

        bool flag = true;

        stack<char> st;
        for (char c : ps) {
            if (c == '(') {
                st.push(c);
            } else {
                if (st.empty() || st.top() != '(') {
                    flag = false;
                    break;
                }
                st.pop();
            }
        }

        if (flag && st.empty()) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}