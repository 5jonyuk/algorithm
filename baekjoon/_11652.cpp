#include <bits/stdc++.h>
using namespace std;

int n;
long long cnt = 0;
long long maxCnt = 0;
long long maxVal = LLONG_MIN;
long long arr[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + n);

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            cnt++;
            continue;
        }
        if (arr[i] == arr[i - 1]) {
            cnt++;
        } else {
            if (maxCnt < cnt) {
                maxCnt = cnt;
                maxVal = arr[i - 1];
            }
            cnt = 1;
        }
    }

    if (maxCnt < cnt) {
        maxVal = arr[n - 1];
    }

    cout << maxVal;
}