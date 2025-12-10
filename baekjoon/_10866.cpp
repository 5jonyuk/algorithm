#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    deque<int> dq;

    while (n--) {
        string cmd;
        cin >> cmd;

        if (cmd == "push_front") {
            int value;
            cin >> value;
            dq.push_front(value);
        } else if (cmd == "push_back") {
            int value;
            cin >> value;
            dq.push_back(value);
        } else if (cmd == "pop_front") {
            if (!dq.empty()) {
                cout << dq.front() << "\n";
                dq.pop_front();
            } else {
                cout << "-1" << "\n";
            }
        } else if (cmd == "pop_back") {
            if (!dq.empty()) {
                cout << dq.back() << "\n";
                dq.pop_back();
            } else {
                cout << "-1" << "\n";
            }
        } else if (cmd == "size") {
            cout << dq.size() << "\n";
        } else if (cmd == "empty") {
            if (dq.empty()) {
                cout << "1" << "\n";
            } else {
                cout << "0" << "\n";
            }
        } else if (cmd == "front") {
            if (!dq.empty()) {
                cout << dq.front() << "\n";
            } else {
                cout << "-1" << "\n";
            }

        } else {
            if (!dq.empty()) {
                cout << dq.back() << "\n";
            } else {
                cout << "-1" << "\n";
            }
        }
    }
}