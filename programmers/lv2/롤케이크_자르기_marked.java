package lv2;

import java.util.*;
import java.util.stream.Collectors;

public class 롤케이크_자르기_marked {
    public int solution(int[] topping) {
        int answer = 0;
        int[] countingTopping = new int[10001];
        Set<Integer> left = new HashSet<>();
        Set<Integer> original = new HashSet<>(Arrays.stream(topping).boxed().collect(Collectors.toSet()));
        int rightToppingCount = original.size();

        for (int i = 0; i < topping.length; i++) {
            countingTopping[topping[i]]++;
        }

        for (int i = 0; i < topping.length - 1; i++) {
            int currentTopping = topping[i];

            left.add(currentTopping);
            countingTopping[currentTopping]--;

            if (countingTopping[currentTopping] == 0) {
                rightToppingCount--;
            }

            if (left.size() == rightToppingCount) {
                answer++;
            }

        }
        return answer;
    }
}
