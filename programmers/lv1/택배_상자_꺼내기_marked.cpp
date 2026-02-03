#include <bits/stdc++.h>

using namespace std;

int solution(int n, int w, int num) {
    int result = 0;
    int targetRow = (num - 1) / w;
    int targetCol;
    if (targetRow % 2 == 0) {
        targetCol = (num - 1) % w;
    } else {
        targetCol = (w - 1) - (num - 1) % w;
    }

    int maxRow = (n - 1) / w;
    for (int r = targetRow; r <= maxRow; r++) {
        int currCol;

        if (r % 2 == 0) {
            currCol = targetCol;
        } else {
            currCol = (w - 1) - targetCol;
        }

        int currNum = r * w + 1 + currCol;

        if (currNum <= n) {
            result++;
        }
    }
    return result;
}