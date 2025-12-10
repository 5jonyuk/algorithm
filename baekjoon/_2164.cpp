#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    queue<int> Q;
    for (int i = 1; i <= n; i++) {
        Q.push(i);
    }

    while (true) {
        if (Q.size() == 1) {
            break;
        }
        int temp;
        Q.pop();
        temp = Q.front();
        Q.push(temp);
        Q.pop();
    }

    cout << Q.front();
}