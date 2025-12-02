#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> freq(1000001);

    int n;
    cin >> n;
    vector<int> arr(n);

    for (int &x : arr)
        cin >> x;

    int target;
    cin >> target;

    int result = 0;
    for (int x : arr) {
        int remainder = target - x;
        if (remainder < 0 || remainder > 1000000) // 범위 체크 out of bound
            continue;
        if (freq[remainder] == 1) {
            result++;
        }
        freq[x] = 1;
    }
    cout << result;
}