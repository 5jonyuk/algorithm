#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> freqArr(101);

    vector<int> arr;
    int x;

    while (cin >> x) {
        if (x == -1) {
            break;
        }
        arr.push_back(x);
    }

    for (int num : arr) {
        int remainder = 100 - num;
        if (freqArr[remainder] == 1) {
            cout << "1" << "\n" << remainder << " " << num;
            break;
        }
        freqArr[num] = 1;
    }
}