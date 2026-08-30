package lv1;

public class 로또의_최고_순위와_최저_순위 {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];

        int matchCnt = 0;
        for (int i = 0; i < lottos.length; i++) {
            for (int j = 0; j < win_nums.length; j++) {
                if (lottos[i] == win_nums[j]) {
                    matchCnt++;
                    break;
                }
            }
        }

        int zeroCnt = 0;
        for (int i = 0; i < lottos.length; i++) {
            if (lottos[i] == 0) {
                zeroCnt++;
            }
        }

        answer[0] = match(matchCnt + zeroCnt);
        answer[1] = match(matchCnt);
        return answer;
    }

    public int match(int count) {
        if (count == 6) {
            return 1;
        }
        if (count == 5) {
            return 2;
        }
        if (count == 4) {
            return 3;
        }
        if (count == 3) {
            return 4;
        }
        if (count == 2) {
            return 5;
        }

        return 6;
    }
}
