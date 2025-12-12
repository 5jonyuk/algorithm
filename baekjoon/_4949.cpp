#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (true) {
        string s;
        getline(cin, s);

        stack<char> S;
        bool flag = true;

        if (s == ".") {
            break;
        }

        for (char c : s) {
            if (c == '(' || c == '[') {
                S.push(c);
            } else if (c == ')') {
                if (S.empty() || S.top() != '(') {
                    flag = false;
                    break;
                }
                S.pop();
            } else if (c == ']') {
                if (S.empty() || S.top() != '[') {
                    flag = false;
                    break;
                }
                S.pop();
            }
        }

        if (flag && S.empty()) {
            cout << "yes" << "\n";
        } else {
            cout << "no" << "\n";
        }
    }
}