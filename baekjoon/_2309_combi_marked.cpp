#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> arr(9);

    for (int &x : arr)
        cin >> x;
    sort(arr.begin(), arr.end());
    vector<int> mask = {0, 0, 1, 1, 1, 1, 1, 1, 1};

    do {
        for (int m : mask)
            cout << m << " ";
        cout << "\n";

        int result = 0;
        for (int i = 0; i < mask.size(); i++) {
            if (mask[i] == 0)
                continue;
            result += arr[i];
        }
        if (result == 100)
            break;
    } while (next_permutation(mask.begin(), mask.end()));

    for (int i = 0; i < mask.size(); i++) {
        if (mask[i] == 1) {
            cout << arr[i] << "\n";
        }
    }
}