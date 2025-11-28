#include <iostream>
#include <vector>

using namespace std;

int func3(int num) {
    for (int i = 1; i * i <= num; i++) {
        if (i * i == num) {
            return 1;
        }
    }
    return 0;
}

int func4(int num) {
    int val = 1;
    while (2 * val <= num) {
        val *= 2;
    }
    return val;
}

int main() {
    // cin과 printf 를 동시에 쓰는 것을 동기화를 끊는 코드 이걸 쓰면
    // cin과 printf를 같이쓰면 절대 안 됨.
    ios::sync_with_stdio(0);

    // 버퍼로 인해 입력과 출력 순서가 꼬이는 걸 허용
    // -> cin을 하기전에 cout 버퍼를 비움
    // why? 온라인 져지에서는 출력 값만 보기에
    cin.tie(0);

    // 가변형 정수 배열 10개 0으로 초기화
    vector<int> v(10);

    int n;

    cin >> n;
    cout << func3(n) << endl;
    cout << func4(n);
}
