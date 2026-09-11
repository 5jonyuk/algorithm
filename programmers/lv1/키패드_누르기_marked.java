package lv1;

import java.util.HashMap;
import java.util.Map;

// StringBuilder
// 배열 참조 조심
public class 키패드_누르기_marked {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        Map<Integer, int[]> keypad = new HashMap<>();

        init(keypad);

        int[] leftNow = new int[] { 0, 0 };
        int[] rightNow = new int[] { 0, 2 };

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
                leftNow = keypad.get(numbers[i]);
                answer.append("L");
            } else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
                rightNow = keypad.get(numbers[i]);
                answer.append("R");
            } else {
                int[] now = keypad.get(numbers[i]);

                int leftDist = Math.abs(now[0] - leftNow[0]) + Math.abs(now[1] - leftNow[1]);
                int rightDist = Math.abs(now[0] - rightNow[0]) + Math.abs(now[1] - rightNow[1]);

                if (leftDist > rightDist) {
                    rightNow = now;
                    answer.append("R");
                } else if (leftDist < rightDist) {
                    leftNow = now;
                    answer.append("L");
                } else {
                    if (hand.equals("right")) {
                        rightNow = now;
                        answer.append("R");
                    } else {
                        leftNow = now;
                        answer.append("L");
                    }
                }
            }
        }
        return answer.toString();
    }

    public void init(Map<Integer, int[]> keypad) {
        keypad.put(1, new int[] { 3, 0 });
        keypad.put(2, new int[] { 3, 1 });
        keypad.put(3, new int[] { 3, 2 });

        keypad.put(4, new int[] { 2, 0 });
        keypad.put(5, new int[] { 2, 1 });
        keypad.put(6, new int[] { 2, 2 });

        keypad.put(7, new int[] { 1, 0 });
        keypad.put(8, new int[] { 1, 1 });
        keypad.put(9, new int[] { 1, 2 });

        keypad.put(0, new int[] { 0, 1 });
    }
}
