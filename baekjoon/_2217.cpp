/*
로프들 중 가장 작은 값이 최대로 들 수 있는 무게는 현재 가장 작은 로프 값 * 현재 로프 수 밖에 안됨
-> 가장 작은 로프부터 시작하여 로프들이 버틸 수 있는 무게를 저장하며 로프들 중 가장 작은 로프를 버림
남겨진 로프들로 위의 과정을 반복
*/

#include <bits/stdc++.h>
using namespace std;

int n;
int rope[100000];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> rope[i];
    }

    sort(rope, rope + n);

    // vector<int> result;
    // int cnt = 0;
    // for (int i = 0; i < n - 1; i++) {
    //     result.push_back(rope[i] * (n - cnt));
    //     cnt++;
    // }
    // result.push_back(rope[n - 1]);
    // cout << *max_element(result.begin(), result.end());

    int result = 0;
    for (int i = 0; i < n; i++) {
        result = max(result, rope[i] * (n - i));
    }

    cout << result;
}