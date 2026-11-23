package lv1;

import java.util.*;

public class 신고_결과_받기_marked {
    private Map<String, Integer> init(String[] id_list) {
        Map<String, Integer> answer = new LinkedHashMap<>();

        for (String id : id_list) {
            answer.put(id, 0);
        }
        return answer;
    }

    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Set<String>> reportMap = new HashMap<>();

        for (String r : report) {
            String[] row = r.split(" ");

            if (!reportMap.containsKey(row[1])) {
                reportMap.put(row[1], new HashSet<>(Set.of(row[0])));
            } else {
                reportMap.get(row[1]).add(row[0]);
            }
        }

        Map<String, Integer> answer = init(id_list);

        for (Map.Entry<String, Set<String>> entry : reportMap.entrySet()) {
            if (entry.getValue().size() >= k) {
                for (String reporter : entry.getValue()) {
                    answer.put(reporter, answer.get(reporter) + 1);
                }
            }
        }

        return answer.values().stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
