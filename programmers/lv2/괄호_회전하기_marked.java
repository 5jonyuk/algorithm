package lv2;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class 괄호_회전하기_marked {
    public boolean check(Deque<Character> dq, Map<Character, Character> map) {
        Deque<Character> result = new ArrayDeque<>();

        for (char c : dq) {
            if (!map.containsKey(c)) {
                result.push(c);
            } else {
                if (result.isEmpty()) {
                    return false;
                }
                if (result.peek() != map.get(c)) {
                    return false;
                }
                result.pop();
            }
        }
        return result.isEmpty();
    }

    public void move(Deque<Character> dq) {
        if (!dq.isEmpty()) {
            char pollChar = dq.pollFirst();
            dq.addLast(pollChar);
        }
    }

    public int solution(String s) {
        Map<Character, Character> map = new HashMap<>();

        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        Deque<Character> deque = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            deque.addLast(s.charAt(i));
        }

        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            if (check(deque, map)) {
                answer++;
            }
            move(deque);
        }

        return answer;
    }
}
