package lv1;

public class 없는_숫자_더하기 {
    public int solution(int[] numbers) {
        int[] answer = new int[10];

        for (int num : numbers) {
            answer[num] = -1;
        }

        int sum = 0;
        for (int i = 1; i < answer.length; i++) {
            if (answer[i] != -1) {
                sum += i;
            }
        }

        return sum;
    }
}
