#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> arr(5); // 변수면 O(n) 사실상 상수시간
    for (int &x : arr)
        cin >> x;

    sort(arr.begin(), arr.end()); // O(nlog n)

    int avg = accumulate(arr.begin(), arr.end(), 0) / arr.size(); // O(n)
    int middle = arr[2];                                          // O(1)

    cout << avg << "\n" << middle; // O(1)
}
// O(nlog n + n) = O(nlog n)