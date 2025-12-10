#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    queue<int> q;

    while (n--) {
        string cmd;
        cin >> cmd;

        if (cmd == "push") {
            int value;
            cin >> value;

            q.push(value);
        } else if (cmd == "pop") {
            if (!q.empty()) {
                cout << q.front() << "\n";
                q.pop();
            } else {
                cout << "-1" << "\n";
            }
        } else if (cmd == "size") {
            cout << q.size() << "\n";
        } else if (cmd == "front") {
            if (!q.empty()) {
                cout << q.front() << "\n";
            } else {
                cout << "-1" << "\n";
            }
        } else if (cmd == "back") {
            if (!q.empty()) {
                cout << q.back() << "\n";
            } else {
                cout << "-1" << "\n";
            }
        } else {
            if (q.empty()) {
                cout << "1" << "\n";
            } else {
                cout << "0" << "\n";
            }
        }
    }
}