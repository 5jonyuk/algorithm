package lv2;

import java.util.Stack;

public class 올바른_괄호_marked {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char braket = s.charAt(i);

            if (braket == '(') {
                stack.push(braket);
            } else {
                if (!stack.isEmpty() && stack.peek().equals('(')) {
                    stack.pop();
                } else {
                    answer = false;
                    break;
                }
            }
        }

        if (stack.size() != 0) {
            answer = false;
        }
        return answer;
    }
}
