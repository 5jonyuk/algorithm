#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> freq(10);
    int result = 0;

    int roomNum;
    cin >> roomNum;

    while (roomNum > 0) {
        freq[roomNum % 10]++;
        roomNum /= 10;
    }

    if ((freq[6] + freq[9]) % 2 == 0) {
        result = (freq[6] + freq[9]) / 2;
    } else {
        result = (freq[6] + freq[9]) / 2 + 1;
    }

    int maxFreq = freq[0];
    for (int i = 1; i < freq.size(); i++) {
        if (i == 6 || i == 9)
            continue;
        if (maxFreq < freq[i]) {
            maxFreq = freq[i];
        }
    }

    if (result < maxFreq) {
        cout << maxFreq;
    } else {
        cout << result;
    }
}