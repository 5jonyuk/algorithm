#include <bits/stdc++.h>
using namespace std;

int n;
int arr[2000001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        if (num < 0) {
            arr[abs(num)]++;
        } else if (num == 0) {
            arr[0]++;
        } else {
            arr[num + 1000000]++;
        }
    }

    for (int i = 1000000; i > 0; i--) {
        if (arr[i] >= 1) {
            for (int j = 0; j < arr[i]; j++) {
                cout << -i << "\n";
            }
        }
    }
    for (int i = 0; i < arr[0]; i++) {
        cout << 0 << "\n";
    }

    for (int i = 1000001; i < 2000001; i++) {
        if (arr[i] >= 1) {
            for (int j = 0; j < arr[i]; j++) {
                cout << i - 1000000 << "\n";
            }
        }
    }
}