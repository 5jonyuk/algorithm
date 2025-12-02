#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> arr(21);
    for (int i = 1; i < arr.size(); i++) {
        arr[i] = i;
    }

    for (int i = 0; i < 10; i++) {
        int a, b;
        cin >> a >> b;

        for (int j = 0; j < (b - a + 1) / 2; j++) {
            swap(arr[a + j], arr[b - j]);
        }
    }
    for (int i = 1; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
}
