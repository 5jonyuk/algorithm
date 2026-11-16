package lv1;

import java.util.HashMap;
import java.util.Map;

public class 실패율 {
    public int[] solution(int N, int[] stages) {
        int[] challenger = new int[N + 2];

        for (int i = 0; i < stages.length; i++) {
            challenger[stages[i]] += 1;
        }

        double total = stages.length;

        Map<Integer, Double> fails = new HashMap<>();

        for (int i = 1; i <= N; i++) {
            if (challenger[i] == 0) {
                fails.put(i, 0.0);
            } else {
                fails.put(i, challenger[i] / total);
                total -= challenger[i];
            }
        }

        return fails.entrySet().stream()
                .sorted((o1, o2) -> Double.compare(o2.getValue(), o1.getValue()))
                .mapToInt(Map.Entry::getKey)
                .toArray();
    }
}
