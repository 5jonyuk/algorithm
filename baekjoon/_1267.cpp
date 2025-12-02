#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> callTimes(n);
    for (int &callTime : callTimes)
        cin >> callTime;

    int yTime = 30;
    int mTime = 60;

    int yCnt, mCnt;
    yCnt = mCnt = 0;

    int yResult, mResult;
    yResult = mResult = 0;

    for (int i = 0; i < n; i++) {
        yCnt += callTimes[i] / yTime + 1;
        mCnt += callTimes[i] / mTime + 1;
    }
    yResult = 10 * yCnt;
    mResult = 15 * mCnt;

    if (yResult == mResult) {
        cout << "Y M " << yResult;
    } else if (yResult > mResult) {
        cout << "M " << mResult;
    } else {
        cout << "Y " << yResult;
    }
}