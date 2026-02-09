#include <bits/stdc++.h>
using namespace std;

int n;
vector<string> arr;

// isdigit() - marked
int extractNum(const string &s) {
    int sum = 0;
    for (char c : s) {
        if (isdigit(c)) {
            sum += c - '0';
        }
    }
    return sum;
}

// bool dictCompare(const string &a, const string &b) {
//     for (int i = 0; i < a.length(); i++) {
//         if (a[i] == b[i]) {
//             continue;
//         } else {
//             // 둘 다 알파벳일 때
//             if (!isdigit(a[i]) && !isdigit(b[i])) {
//                 return a[i] < b[i];
//             }
//             // 둘 다 숫자일 때
//             if (isdigit(a[i]) && isdigit(b[i])) {
//                 return a[i] < b[i];
//             }
//             // 두 개가 다를 때 (marked)
//             if (isdigit(a[i]) && !isdigit(b[i])) {
//                 return true;
//             }
//             if (!isdigit(a[i]) && isdigit(b[i])) {
//                 return false;
//             }
//         }
//     }
//     return false;
// }

bool cmp(const string &a, const string &b) {
    if (a.length() < b.length())
        return true;
    if (a.length() == b.length() && extractNum(a) != extractNum(b)) {
        return extractNum(a) < extractNum(b);
    }
    if (a.length() == b.length() && extractNum(a) == extractNum(b)) {
        return a < b; // string을 비교할 땐 기본적으로 사전 순 비교
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        string serial;
        cin >> serial;
        arr.push_back(serial);
    }

    sort(arr.begin(), arr.end(), cmp);

    for (string s : arr) {
        cout << s << "\n";
    }
}