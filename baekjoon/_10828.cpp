#include <bits/stdc++.h>
using namespace std;

bool isEmpty(stack<int> S) {
    if (S.empty())
        return true;
    else
        return false;
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    stack<int> S;
    while (n-- > 0) {
        string op;
        cin >> op;

        if (op == "push") {
            int num;
            cin >> num;
            S.push(num);
        } else if (op == "top") {
            if (!isEmpty(S)) {
                cout << S.top() << "\n";
            } else
                cout << "-1" << "\n";
        } else if (op == "size") {
            cout << S.size() << "\n";
        } else if (op == "empty") {
            if (!isEmpty(S)) {
                cout << "0" << "\n";
            } else
                cout << "1" << "\n";
        } else {
            if (!isEmpty(S)) {
                cout << S.top() << "\n";
                S.pop();
            } else
                cout << "-1" << "\n";
        }
    }
}