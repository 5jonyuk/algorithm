package lv1;

import java.util.ArrayList;
import java.util.List;

public class 둘만의_암호 {
    public String solution(String s, String skip, int index) {
        List<String> alpha = new ArrayList<>(
                List.of("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"));
        String answer = "";

        for (int i = 0; i < skip.length(); i++) {
            alpha.remove(String.valueOf(skip.charAt(i)));
        }

        for (int i = 0; i < s.length(); i++) {
            int findIdx = (alpha.indexOf(String.valueOf(s.charAt(i))) + index) % alpha.size();
            answer += alpha.get(findIdx);
        }
        return answer;
    }
}
