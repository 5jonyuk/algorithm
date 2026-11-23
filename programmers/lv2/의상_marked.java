package lv2;

import java.util.*;

public class 의상_marked {
    public int solution(String[][] clothes) {
        Map<String, List<String>> clothesMap = new HashMap<>();

        for (String[] cloth : clothes) {
            if (clothesMap.containsKey(cloth[1])) {
                clothesMap.get(cloth[1]).add(cloth[0]);
            } else {
                clothesMap.put(cloth[1], new ArrayList<>(List.of(cloth[0])));
            }
        }

        int answer = 1;
        for (Map.Entry<String, List<String>> entry : clothesMap.entrySet()) {
            answer *= entry.getValue().size() + 1;
        }

        return answer - 1;
    }
}
