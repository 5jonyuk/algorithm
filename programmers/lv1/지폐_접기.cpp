#include <bits/stdc++.h>
using namespace std;

void folidngAndRotate(int &x, int &y, int &answer) {
    if (x > y) {
        x /= 2;
    } else {
        y /= 2;
    }
    answer++;
    swap(x, y);
}

int solution(vector<int> wallet, vector<int> bill) {
    int answer = 0;

    while (max(wallet[0], wallet[1]) < max(bill[0], bill[1]) || min(wallet[0], wallet[1]) < min(bill[0], bill[1])) {
        folidngAndRotate(bill[0], bill[1], answer);
    }

    return answer;
}