// sort의 cmp 활용
#include <bits/stdc++.h>
using namespace std;

int sort_idx = 0;

int findIdx(string str) {
    if (str == "code") {
        return 0;
    }
    if (str == "date") {
        return 1;
    }
    if (str == "maximum") {
        return 2;
    }
    if (str == "remain") {
        return 3;
    }
}

bool cmp(vector<int> &a, vector<int> &b) { return a[sort_idx] < b[sort_idx]; }

vector<vector<int>> solution(vector<vector<int>> data, string ext, int val_ext, string sort_by) {
    vector<vector<int>> answer;
    int idx = findIdx(ext);

    for (int i = 0; i < data.size(); i++) {
        if (data[i][idx] <= val_ext) {
            answer.push_back(data[i]);
        }
    }

    // int sort_idx = findIdx(sort_by);
    // sort(answer.begin(), answer.end(),
    //      [sort_idx](vector<int> &a, vector<int> &b) { return a[sort_idx] < b[sort_idx]; });

    sort_idx = findIdx(sort_by);
    sort(answer.begin(), answer.end(), cmp);

    return answer;
}