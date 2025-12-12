#include <bits/stdc++.h>
using namespace std;

int main() {
    ios ::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    stack<int> st;

    for (char c : s) {
        if (c == '(') {
            st.push(-1);
        } else if (c == '[') {
            st.push(-2);
        } else if (c == ')') {
            if (st.empty()) {
                cout << 0;
                return 0;
            }

            int sum = 0;
            while (!st.empty() && st.top() > 0) {
                sum += st.top();
                st.pop();
            }

            if (st.empty() || st.top() != -1) {
                cout << 0;
                return 0;
            }

            st.pop();

            if (sum == 0) {
                st.push(2);
            } else {
                st.push(sum * 2);
            }

        } else if (c == ']') {
            if (st.empty()) {
                cout << 0;
                return 0;
            }

            int sum = 0;
            while (!st.empty() && st.top() > 0) {
                sum += st.top();
                st.pop();
            }

            if (st.empty() || st.top() != -2) {
                cout << 0;
                return 0;
            }

            st.pop();

            if (sum == 0) {
                st.push(3);
            } else {
                st.push(sum * 3);
            }
        }
    }

    int ans = 0;
    while (!st.empty()) {
        if (st.top() < 0) {
            cout << 0;
            return 0;
        }
        ans += st.top();
        st.pop();
    }
    cout << ans;
}