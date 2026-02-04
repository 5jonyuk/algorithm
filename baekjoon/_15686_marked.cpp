// // 백트래킹
// #include <bits/stdc++.h>
// using namespace std;
// #define X first
// #define Y second

// int n;
// int m;
// int city[51][51];
// vector<pair<int, int>> houses;
// vector<pair<int, int>> chickens;
// vector<pair<int, int>> selected;
// int ans = int(1e9);

// int calcCityChickenDistance(vector<pair<int, int>> &selected) {
//     int cityChickenDistance = 0;

//     for (auto house : houses) {
//         int chickenDistance = int(1e9);
//         for (auto select : selected) {
//             chickenDistance = min(chickenDistance, (abs(select.X - house.X) + abs(select.Y - house.Y)));
//         }
//         cityChickenDistance += chickenDistance;
//     }
//     return cityChickenDistance;
// }

// void backtrack(int idx, vector<pair<int, int>> &selected) {
//     if (selected.size() == m) {
//         ans = min(ans, calcCityChickenDistance(selected));
//         return;
//     }
//     if (idx == chickens.size()) {
//         return;
//     }

//     selected.push_back(chickens[idx]);
//     backtrack(idx + 1, selected);
//     selected.pop_back();
//     backtrack(idx + 1, selected);

//     return;
// }

// int main() {
//     ios::sync_with_stdio(0);
//     cin.tie(0);

//     cin >> n >> m;

//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             cin >> city[i][j];
//             if (city[i][j] == 1) {
//                 houses.push_back({i, j});
//             } else if (city[i][j] == 2) {
//                 chickens.push_back({i, j});
//             }
//         }
//     }

//     backtrack(0, selected);

//     cout << ans;
// }

// 조합 (next_permutation)
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int n, m;
int city[51][51];
vector<pair<int, int>> houses;
vector<pair<int, int>> chickens;

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> city[i][j];
            if (city[i][j] == 1) {
                houses.push_back({i, j});
            } else if (city[i][j] == 2) {
                chickens.push_back({i, j});
            }
        }
    }

    vector<int> temp(chickens.size(), 1);
    for (int i = 0; i < temp.size() - m; i++) {
        temp[i] = 0;
    }

    int answer = 0x7f7f7f7f;
    do {
        int cityChickenDistance = 0;
        for (auto house : houses) {
            int chickenDistance = 0x7f7f7f7f;
            for (int i = 0; i < chickens.size(); i++) {
                if (temp[i] == 0) {
                    continue;
                }
                chickenDistance = min(chickenDistance, (abs(chickens[i].X - house.X) + abs(chickens[i].Y - house.Y)));
            }
            cityChickenDistance += chickenDistance;
        }
        answer = min(answer, cityChickenDistance);
    } while (next_permutation(temp.begin(), temp.end()));

    cout << answer;
}