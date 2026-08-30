package lv1;

public class 약수의_개수와_덧셈 {
    public int solution(int left, int right) {
        int answer = 0;

        for (int i = left; i <= right; i++) {
            if (checkPlus(i)) {
                answer += i;
            } else {
                answer -= i;
            }
        }
        return answer;
    }

    public boolean checkPlus(int num) {
        int factorCnt = 0;
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                factorCnt++;
            }
        }
        if (factorCnt % 2 == 0) {
            return true;
        }
        return false;
    }
}
