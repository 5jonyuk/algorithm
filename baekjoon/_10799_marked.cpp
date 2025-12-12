#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string input;
    getline(cin, input);

    vector<char> s(input.begin(), input.end());
    stack<char> stack;

    int ans = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            stack.push(s[i]);
        } else {
            if (s[i - 1] == '(') {
                stack.pop();
                ans += stack.size();
            } else {
                stack.pop();
                ans += 1;
            }
        }
    }
    cout << ans;
}