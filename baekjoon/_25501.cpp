#include <bits/stdc++.h>
using namespace std;

int cnt = 0;

// string이나 vector와 같이 값이 크거나 바뀌지 않는 값이면 참조로 넘기기
int recursion(const string &s, int l, int r) {
    cnt++;
    if (l >= r)
        return 1;
    else if (s[l] != s[r])
        return 0;
    else
        return recursion(s, l + 1, r - 1);
}

int isPalindrome(const string &s) { return recursion(s, 0, s.size() - 1); }

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        cout << isPalindrome(s) << " " << cnt << "\n";
        cnt = 0;
    }
}