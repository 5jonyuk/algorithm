#include <bits/stdc++.h>
using namespace std;

int n;
long long arr[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);

    int cnt = 0;
    int maxCnt = 0;
    long long maxVal = LONG_MIN;

    for (int i = 0; i < n; i++) {
        if (i == 0 || arr[i] == arr[i - 1]) {
            cnt++;
            continue;
        } else {
            if (cnt > maxCnt) {
                maxVal = arr[i - 1];
                maxCnt = cnt;
            }
            cnt = 1;
        }
    }
    if (cnt > maxCnt) {
        maxVal = arr[n - 1];
    }

    cout << maxVal;
}