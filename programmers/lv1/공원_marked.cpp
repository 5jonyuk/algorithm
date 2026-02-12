/* 완전 탐색 */
/*
시간복잡도 분석
M: 돗자리 종류의 개수 (mats.size())
R: 공원의 세로 길이 (park.size())
C: 공원의 가로 길이 (park[0].size())
L: 돗자리의 한 변의 길이 (matsLen)

상세 분석
1. 돗자리 루프(M):
가장 큰 돗자리부터 하나씩 꺼내어 검사합니다.
최악의 경우 모든 돗자리를 다 확인해야 하므로 mats.size()만큼 반복합니다.

2. 공원 탐색 루프(R * C):
check 함수 내에서 돗자리를 놓을 시작점(i, j)을 찾기 위해 공원 전체를 훑습니다.
대략 (R-L) * (C-L) 번 반복하며, 이는 공원 넓이에 비례합니다.

3. 돗자리 영역 확인 루프 (L^2):
시작점을 잡은 후, 해당 위치에서 돗자리 크기(L * L)만큼 실제로 비어있는지(-1) 일일이 확인합니다.
이 루프들이 중첩되어 있기 때문에 전체 연산 횟수는 이들을 모두 곱한 값이 됩니다.

-> O(M * R * C * L^2) = O(10 * 50 * 50 * 10^2)
*/

#include <bits/stdc++.h>
using namespace std;

bool check(vector<vector<string>> &park, int matsLen) {
    if (park.size() < matsLen || park[0].size() < matsLen) {
        return false;
    }

    for (int i = 0; i <= park.size() - matsLen; i++) {
        for (int j = 0; j <= park[i].size() - matsLen; j++) {
            bool isAvailable = true;
            for (int k = i; k < i + matsLen; k++) {
                for (int l = j; l < j + matsLen; l++) {
                    if (park[k][l] != "-1") {
                        isAvailable = false;
                        break;
                    }
                }
                if (!isAvailable) {
                    break;
                }
            }
            if (!isAvailable) {
                continue;
            }
            return true; // 돗자리 필 곳 찾음
        }
    }
    return false; // for문을 다 돌았다는 것은 돗자리를 필 곳이 없다는 뜻
}

int solution(vector<int> mats, vector<vector<string>> park) {
    int answer = 0;
    sort(mats.begin(), mats.end(), greater<int>());

    for (int i = 0; i < mats.size(); i++) {
        if (check(park, mats[i])) {
            answer = mats[i];
            return answer;
        }
    }

    return -1;
}

/* dp 방식 */

// #include <bits/stdc++.h>
// using namespace std;

// int solution(vector<int> mats, vector<vector<string>> park) {
//     int answer = 0;
//     int row = park.size();
//     int col = park[0].size();
//     vector<vector<int>> dp(row, vector<int>(col, 0));

//     for (int i = 0; i < row; i++) {
//         for (int j = 0; j < col; j++) {
//             if (park[i][j] == "-1") {
//                 if (i == 0 || j == 0) {
//                     dp[i][j] = 1;
//                 } else {
//                     dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
//                 }
//                 answer = max(answer, dp[i][j]);
//             }
//         }
//     }

//     sort(mats.begin(), mats.end(), greater<int>());

//     for (int i = 0; i < mats.size(); i++) {
//         if (answer >= mats[i]) {
//             return mats[i];
//         }
//     }
//     return -1;
// }