#include <bits/stdc++.h>
using namespace std;

int solution(vector<vector<string>> board, int h, int w) {
    int answer = 0;
    int boardSize = board.size();
    int dh[4] = {1, -1, 0, 0};
    int dw[4] = {0, 0, -1, 1};

    for (int i = 0; i < 4; i++) {
        int nh = dh[i] + h;
        int nw = dw[i] + w;

        if (nh >= 0 && nh < boardSize && nw >= 0 && nw < boardSize) {
            if (board[h][w] == board[nh][nw]) {
                answer++;
            }
        }
    }

    return answer;
}
