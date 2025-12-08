#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s1, s2;
    cin >> s1 >> s2;

    vector<int> freq1(26);
    vector<int> freq2(26);

    for (char c : s1) {
        freq1[c - 'a']++;
    }
    for (char c : s2) {
        freq2[c - 'a']++;
    }

    int answer = 0;
    for (int i = 0; i < 26; i++) {
        // if (freq1[i] == 0 || freq2[i] == 0) {
        //     answer += freq1[i] + freq2[i];
        // } else {
        //     if (freq1[i] != freq2[i]) {
        //         int diff = abs(freq1[i] - freq2[i]);
        //         answer += diff;
        //     }
        // }
        int diff = abs(freq1[i] - freq2[i]);
        answer += diff;
    }
    cout << answer;
}