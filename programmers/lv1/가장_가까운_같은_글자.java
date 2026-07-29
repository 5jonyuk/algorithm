package lv1;

import java.util.*;

public class 가장_가까운_같은_글자 {
    public int[] solution(String s) {
        List<Integer> list = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();

        for (char ch = 'a'; ch <= 'z'; ch++) {
            map.put(ch, -1);
        }

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (map.get(c) == -1) {
                map.put(c, i);
                list.add(-1);
            } else {
                list.add(i - map.get(c));
                map.put(c, i);
            }
        }

        return list.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
