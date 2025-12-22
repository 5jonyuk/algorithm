#include <bits/stdc++.h>
using namespace std;

void hanoi(int start, int mid, int end, int n) {
    if (n == 1) {
        cout << start << " " << end << "\n";
        return;
    }
    hanoi(start, end, mid, n - 1);
    cout << start << " " << end << "\n";
    hanoi(mid, start, end, n - 1);
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    cout << (1 << n) - 1 << "\n"; // 1을 비트 기준으로 n칸 민다. 즉 2의 n승, 하노이 탑의 이동 횟수를 표현
    hanoi(1, 2, 3, n);
}