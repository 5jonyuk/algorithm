#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    stack<int> s;
    int start = 0;

    // vector<char> result;
    string ans;

    while (n--) {
        int num;
        cin >> num;

        if (start < num) {
            for (start = start + 1; start <= num; start++) {
                s.push(start);
                // result.push_back('+');
                ans += "+\n";
            }
            start = num;
        } else if (s.top() != num) {
            cout << "NO" << "\n";
            return 0;
        }
        s.pop();
        ans += "-\n";
    }

    // for (char r : result) {
    //     cout << r << "\n";
    // }
    cout << ans;
}