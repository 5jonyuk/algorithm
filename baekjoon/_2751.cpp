#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1000001];
int temp[1000001];

void merge(int start, int end) {
    int mid = (start + end) / 2;

    int lidx = start;
    int ridx = mid;

    for (int i = start; i < end; i++) {
        if (ridx == end) {
            temp[i] = arr[lidx++];
        } else if (lidx == mid) {
            temp[i] = arr[ridx++];
        } else if (arr[lidx] <= arr[ridx]) {
            temp[i] = arr[lidx++];
        } else {
            temp[i] = arr[ridx++];
        }
    }

    for (int i = start; i < end; i++) {
        arr[i] = temp[i];
    }
}

void merge_sort(int start, int end) {
    if (end - start == 1) {
        return;
    }

    int mid = (start + end) / 2;

    merge_sort(start, mid);
    merge_sort(mid, end);
    merge(start, end);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // sort(arr.begin(), arr.end());
    merge_sort(0, n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << "\n";
    }
}