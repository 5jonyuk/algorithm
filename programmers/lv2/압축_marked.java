package lv2;

import java.util.*;

public class 압축_marked {
    private Map<String, Integer> init() {
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < 26; i++) {
            map.put(String.valueOf((char) ('A' + i)), i + 1);
        }

        return map;
    }

    public int[] solution(String msg) {

        Map<String, Integer> alphabet = init();
        List<Integer> answer = new ArrayList<>();

        String nextAlphabet = "";
        for (int i = 0; i < msg.length(); i++) {
            String nowAlphabet = String.valueOf(msg.charAt(i));

            nextAlphabet += nowAlphabet;
            if (!alphabet.containsKey(nextAlphabet)) {
                String prevAlpha = nextAlphabet.substring(0, nextAlphabet.length() - 1);
                answer.add(alphabet.get(prevAlpha));
                alphabet.put(nextAlphabet, alphabet.size() + 1);
                nextAlphabet = nowAlphabet;
            }
        }
        answer.add(alphabet.get(nextAlphabet));

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
