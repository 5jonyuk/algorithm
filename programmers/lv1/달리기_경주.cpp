#include <bits/stdc++.h>

using namespace std;

// vector<string> solution(vector<string> players, vector<string> callings) {
//     unordered_map<string, int> rank;

//     for (int i = 0; i < players.size(); i++) {
//         rank[players[i]] = i;
//     }

//     for (int i = 0; i < callings.size(); i++) {
//         int findIdx = rank[callings[i]];
//         int targetIdx = findIdx - 1;
//         string targetName = players[targetIdx];
//         rank[callings[i]] = targetIdx;
//         rank[targetName] = findIdx;
//         swap(players[findIdx], players[targetIdx]);
//     }

//     return players;
// }

// 가독성 향상 버전
vector<string> solution(vector<string> players, vector<string> callings) {
    unordered_map<string, int> rank;

    for (int i = 0; i < players.size(); i++) {
        rank[players[i]] = i;
    }

    for (string &name : callings) {
        int currentIndex = rank[name];
        int frontIndex = currentIndex - 1;

        string frontPlayer = players[frontIndex];

        rank[name] = frontIndex;
        rank[frontPlayer] = currentIndex;
        swap(players[currentIndex], players[frontIndex]);
    }

    return players;
}