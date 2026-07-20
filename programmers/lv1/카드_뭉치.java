package lv1;

import java.util.*;

public class 카드_뭉치 {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        int cards1_idx = 0;
        int cards2_idx = 0;

        for (int i = 0; i < goal.length; i++) {
            String target = goal[i];

            if (cards1_idx < cards1.length && cards1[cards1_idx].equals(target)) {
                cards1_idx++;
                continue;
            }
            if (cards2_idx < cards2.length && cards2[cards2_idx].equals(target)) {
                cards2_idx++;
                continue;
            }

            answer = "No";
            break;
        }
        return answer;
    }
}
