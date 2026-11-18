package lv2;

import java.util.HashMap;
import java.util.Map;

public class 할인_행사_marked {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }

        int i = 0;
        while (i + 9 < discount.length) {
            Map<String, Integer> target = new HashMap<>();

            for (int j = i; j < i + 10; j++) {
                target.put(
                        discount[j],
                        target.getOrDefault(discount[j], 0) + 1);
            }

            boolean breakFlag = false;
            for (String s : want) {
                if (!map.get(s).equals(target.get(s))) {
                    breakFlag = true;
                    break;
                }
            }
            if (!breakFlag) {
                answer++;
            }
            i++;
        }
        return answer;
    }
}
