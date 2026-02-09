#include <bits/stdc++.h>
using namespace std;

int arr[8] = {1, 5, 4, 2, 3, 1, 4, 3};
int count_arr[6] = {};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for (int i = 0; i < 8; i++) {
        count_arr[arr[i]]++;
    }

    for (int i = 1; i < 6; i++) {
        for (int j = 0; j < count_arr[i]; j++) {
            cout << i << " ";
        }
    }
}