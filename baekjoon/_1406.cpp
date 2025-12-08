#include <bits/stdc++.h>
using namespace std;

int unused = 1;
const int MX = 1000000;
char dat[MX];
int pre[MX], nxt[MX];

void insert(int addr, char c) {
    dat[unused] = c;

    pre[unused] = addr;
    nxt[unused] = nxt[addr];

    if (nxt[addr] != -1) {
        pre[nxt[addr]] = unused;
    }
    nxt[addr] = unused;

    unused++;
}

void erase(int addr) {
    if (nxt[addr] != -1) {
        pre[nxt[addr]] = pre[addr];
    }
    nxt[pre[addr]] = nxt[addr];
}

void traverse() {
    int curr = nxt[0];
    while (curr != -1) {
        cout << dat[curr] << "";
        curr = nxt[curr];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;

    // STL
    // list<char> L;
    // for (char c : s) {
    //     L.push_back(c);
    // }

    // auto cursor = L.end();

    // int n;
    // cin >> n;

    // for (int i = 0; i < n; i++) {
    //     char cmd;
    //     cin >> cmd;

    //     if (cmd == 'P') {
    //         char value;
    //         cin >> value;
    //         L.insert(cursor, value);
    //     } else if (cmd == 'L') {
    //         if (cursor != L.begin()) {
    //             cursor--;
    //         }
    //     } else if (cmd == 'D') {
    //         if (cursor != L.end()) {
    //             cursor++;
    //         }
    //     } else {
    //         if (cursor != L.begin()) {
    //             cursor--;
    //             cursor = L.erase(cursor);
    //         }
    //     }
    // }
    // for (char c : L) {
    //     cout << c << "";
    // }

    // 야매

    fill(pre, pre + MX, -1);
    fill(nxt, nxt + MX, -1);

    int cursor = 0;

    for (char c : s) {
        insert(cursor, c);
        cursor++;
    }

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        char cmd;
        cin >> cmd;

        if (cmd == 'P') {
            char value;
            cin >> value;
            insert(cursor, value);
            cursor = nxt[cursor];
        } else if (cmd == 'L') {
            if (pre[cursor] != -1) {
                cursor = pre[cursor];
            }
        } else if (cmd == 'D') {
            if (nxt[cursor] != -1) {
                cursor = nxt[cursor];
            }
        } else {
            if (cursor != 0) {
                erase(cursor);
                cursor = pre[cursor];
            }
        }
    }
    traverse();
}