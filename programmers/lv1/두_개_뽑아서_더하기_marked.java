package lv1;

import java.util.*;

public class 두_개_뽑아서_더하기_marked {
    // public int[] solution(int[] numbers) {
    // List<Integer> answer = new ArrayList<>();

    // for (int i = 0; i < numbers.length; i++) {
    // for (int j = i + 1; j < numbers.length; j++) {
    // if (!answer.contains(numbers[i] + numbers[j])) {
    // answer.add(numbers[i] + numbers[j]);
    // }
    // }
    // }
    // return answer.stream()
    // .sorted()
    // .mapToInt(Integer::intValue)
    // .toArray();
    // }

    public int[] solution(int[] numbers) {
        Set<Integer> answer = new TreeSet<>();

        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                answer.add(numbers[i] + numbers[j]);
            }
        }

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
