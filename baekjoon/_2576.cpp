#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n = 7;
    int result = 0;
    int min_num = 101;

    while (n-- > 0) {
        int x;
        cin >> x;
        if (x % 2 != 0) {
            result += x;
            min_num = min(min_num, x);
        }
    }

    if (result == 0) {
        cout << -1;
        return 0;
    }
    cout << result << "\n" << min_num;
}