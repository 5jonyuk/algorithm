package lv1;

import java.util.*;

public class 햄버거_만들기_marked {
    public int solution(int[] ingredient) {
        int answer = 0;

        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < ingredient.length; i++) {
            deque.push(ingredient[i]);

            if (deque.size() >= 4) {
                Iterator<Integer> it = deque.iterator();
                int first = it.next();
                int second = it.next();
                int third = it.next();
                int fourth = it.next();

                if (first == 1 && second == 3 && third == 2 && fourth == 1) {
                    for (int j = 0; j < 4; j++) {
                        deque.pop();
                    }
                    answer++;
                }
            }
        }
        return answer;
    }
}
