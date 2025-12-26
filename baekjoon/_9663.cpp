#include <bits/stdc++.h>
using namespace std;

int n;
int isUsedCol[15];
int isUsedBottomToTopDiagonal[30];
int isUsedTopToBottomDiagonal[30];
int cnt = 0;

void backtrack(int row) {
    if (row == n) {
        cnt++;
        return;
    }

    for (int i = 0; i < n; i++) {
        if (isUsedCol[i] || isUsedBottomToTopDiagonal[row + i] || isUsedTopToBottomDiagonal[row - i + n - 1]) {
            continue;
        }

        isUsedCol[i] = 1;
        isUsedBottomToTopDiagonal[row + i] = 1;
        isUsedTopToBottomDiagonal[row - i + n - 1] = 1;
        backtrack(row + 1);
        isUsedCol[i] = 0;
        isUsedBottomToTopDiagonal[row + i] = 0;
        isUsedTopToBottomDiagonal[row - i + n - 1] = 0;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    backtrack(0);
    cout << cnt;
}

// #include <bits/stdc++.h>
// using namespace std;

// int n;
// int queen[15];
// int cnt = 0;

// bool check(int row) {
//     for (int i = 0; i < row; i++) {
//         if (queen[row] == queen[i] || abs(row - i) == abs(queen[row] - queen[i])) {
//             return false;
//         }
//     }
//     return true;
// }

// void backtrack(int row) {
//     if (row == n) {
//         cnt++;
//         return;
//     }

//     for (int col = 0; col < n; col++) {
//         queen[row] = col;
//         if (check(row)) {
//             backtrack(row + 1);
//         }
//     }
// }

// int main() {
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     cin >> n;

//     backtrack(0);
//     cout << cnt;
// }