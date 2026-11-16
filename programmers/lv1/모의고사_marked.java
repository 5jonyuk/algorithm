package lv1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 모의고사_marked {
    public int[] solution(int[] answers) {
        int[][] patterns = {
                { 1, 2, 3, 4, 5 },
                { 2, 1, 2, 3, 2, 4, 2, 5 },
                { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 }
        };

        int[] scores = new int[3];

        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < patterns.length; j++) {
                if (answers[i] == patterns[j][i % patterns[j].length]) {
                    scores[j]++;
                }
            }
        }
        int maxScore = Arrays.stream(scores)
                .max()
                .getAsInt();

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            if (scores[i] == maxScore) {
                result.add(i + 1);
            }
        }

        return result.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
