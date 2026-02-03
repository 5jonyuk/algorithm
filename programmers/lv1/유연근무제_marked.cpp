#include <bits/stdc++.h>

using namespace std;

int toMinute(int time) { return (time / 100) * 60 + time % 100; }

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = 0;

    for (int i = 0; i < schedules.size(); i++) {
        bool target = true;
        for (int j = startday; j < startday + 7; j++) {
            if (j % 7 == 6 || j % 7 == 0) {
                continue;
            }
            int idx = j - startday;
            if (toMinute(timelogs[i][idx]) - toMinute(schedules[i]) > 10) {
                target = false;
                break;
            }
        }
        if (target) {
            answer++;
        }
    }
    return answer;
}