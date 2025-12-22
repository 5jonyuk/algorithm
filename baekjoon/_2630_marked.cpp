#include <bits/stdc++.h>
using namespace std;

int paper[130][130];
int cnt[2];

bool check(int x, int y, int s) {
    for (int i = x; i < x + s; i++) {
        for (int j = y; j < y + s; j++) {
            if (paper[x][y] != paper[i][j]) {
                return false;
            }
        }
    }
    cnt[paper[x][y]]++;
    return true;
}

void split_paper(int x, int y, int size) {
    if (check(x, y, size)) {
        return;
    }
    size /= 2;

    split_paper(x, y, size);
    split_paper(x, y + size, size);
    split_paper(x + size, y, size);
    split_paper(x + size, y + size, size);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> paper[i][j];
        }
    }

    split_paper(0, 0, n);

    cout << cnt[0] << "\n";
    cout << cnt[1] << "\n";
}