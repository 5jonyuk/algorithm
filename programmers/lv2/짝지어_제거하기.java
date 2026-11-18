package lv2;

import java.util.ArrayDeque;
import java.util.Deque;

public class 짝지어_제거하기 {
    public int solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (stack.isEmpty()) {
                stack.push(c);
            } else {
                if (stack.peek() != c) {
                    stack.push(c);
                } else {
                    stack.pop();
                }
            }
        }
        if (stack.isEmpty()) {
            return 1;
        }
        return 0;
    }
}
