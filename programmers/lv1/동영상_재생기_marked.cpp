#include <bits/stdc++.h>

using namespace std;

int parseToTime(string time) {
    // stringstream ss(time);
    // string token;
    // vector<string> result;

    // while (getline(ss, token, ':')) {
    //     result.push_back(token);
    // }

    // int min = stoi(result[0]);
    // int sec = stoi(result[1]);

    int min = stoi(time.substr(0, 2)); // 0번 인덱스에서부터 2개
    int sec = stoi(time.substr(3, 2)); // 3번 인덱스에서부터 2개

    return min * 60 + sec;
}

string parseToString(int time) {
    string min = to_string(time / 60);
    string sec = to_string(time % 60);

    if (min.length() < 2) {
        min = "0" + min;
    }
    if (sec.length() < 2) {
        sec = "0" + sec;
    }

    return min + ":" + sec;
}

// position의 주소값을 넘겨 함수 리턴 후에도 값이 유지되게 함
void openingCheck(int &position, int start, int end) {
    if (position >= start && position <= end) {
        position = end;
    }
}

string solution(string video_len, string pos, string op_start, string op_end, vector<string> commands) {
    int videoLen = parseToTime(video_len);
    int position = parseToTime(pos);
    int start = parseToTime(op_start);
    int end = parseToTime(op_end);

    openingCheck(position, start, end);

    for (string cmd : commands) {
        if (cmd == "next") {
            if (position + 10 >= videoLen) {
                position = videoLen;
                continue;
            }
            position += 10;
            openingCheck(position, start, end);
        } else {
            if (position - 10 <= 0) {
                position = 0;
                openingCheck(position, start, end);
                continue;
            }
            position -= 10;
            openingCheck(position, start, end);
        }
    }

    openingCheck(position, start, end);

    return parseToString(position);
}