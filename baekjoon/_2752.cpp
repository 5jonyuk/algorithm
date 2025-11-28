#include <bits/stdc++.h>
using namespace std;

// int main() {

//     vector<int> v(3);
//     for (int i = 0; i < 3; i++) {
//         cin >> v[i];
//     }

//     for (int i = 0; i < 3; i++) {
//         int temp = 0;
//         for (int j = i + 1; j < 3; j++) {
//             if (v[i] > v[j]) {
//                 temp = v[i];
//                 v[i] = v[j];
//                 v[j] = temp;
//             }
//         }
//     }
//     for (int i = 0; i < 3; i++) {
//         cout << v[i] << " ";
//     }
// }

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> v(3);
    for (int &x : v)
        cin >> x;

    sort(v.begin(), v.end());

    for (int i : v) {
        cout << i << " ";
    }
}