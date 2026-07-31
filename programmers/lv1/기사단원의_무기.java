package lv1;

public class 기사단원의_무기 {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] measures = new int[number + 1];

        for (int i = 1; i <= number; i++) {
            int measureCnt = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    measureCnt++;
                }
            }
            if (measureCnt > limit) {
                measures[i] = power;
                continue;
            }
            measures[i] = measureCnt;
        }

        for (int i = 1; i < measures.length; i++) {
            answer += measures[i];
        }
        return answer;
    }
}
