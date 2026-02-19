#include <bits/stdc++.h>
using namespace std;

int n, m, l;
vector<int> v;

bool check(int mid) {
    int cnt = 0;
    for (int i = 1; i < v.size(); i++) {
        int dist = v[i] - v[i - 1];
        cnt += dist / mid;
        if (dist % mid == 0) {
            cnt--;
        }
    }

    if (cnt > m) {
        /*
        cnt > m의 의미는
        휴게소가 없는 모든 구간에서 휴게소를 세울 수 있는 총 갯수가 내가 지어야하는 휴게소 갯수(m)보다 크다는 의미이며
        즉, mid의 값을 늘려야한다는 것을 의미하며 오른쪽으로 이동시키기 위해 true를 리턴
        */
        return true;
    } else {
        return false;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m >> l;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        v.push_back(x);
    }
    v.push_back(0);
    v.push_back(l);

    sort(v.begin(), v.end());

    int start = 1;
    int end = l;

    int result = 0;
    while (start <= end) {
        int mid = (start + end) / 2; // 시험해볼 허용 가능한 최대 간격

        if (check(mid)) {
            start = mid + 1;
        } else {
            result = mid;
            end = mid - 1;
        }
    }
    cout << result;
}