#include <bits/stdc++.h>
using namespace std;

int n, m;

int arr1[1000001] = {};
int arr2[1000001] = {};
vector<int> answer;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }

    for (int i = 0; i < m; i++) {
        cin >> arr2[i];
    }

    int idx1 = 0;
    int idx2 = 0;

    while (true) {
        if (idx1 == n || idx2 == m) {
            break;
        }
        if (arr1[idx1] < arr2[idx2]) {
            answer.push_back(arr1[idx1++]);
        } else {
            answer.push_back(arr2[idx2++]);
        }
    }

    if (idx1 == n) {
        for (int i = idx2; i < m; i++) {
            answer.push_back(arr2[i]);
        }
    } else if (idx2 == m) {
        for (int i = idx1; i < n; i++) {
            answer.push_back(arr1[i]);
        }
    }

    for (int x : answer) {
        cout << x << " ";
    }
}