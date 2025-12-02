#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> arr(9);
    for (int &num : arr)
        cin >> num;

    int maxIdx, maxNum;
    maxIdx = maxNum = 0;

    for (int i = 1; i < arr.size(); i++) {
        if (arr[maxIdx] < arr[i]) {
            maxIdx = i;
            maxNum = arr[maxIdx];
        }
    }
    maxNum = arr[maxIdx];
    cout << maxNum << "\n" << maxIdx + 1;
}