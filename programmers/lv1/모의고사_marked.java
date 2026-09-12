package lv1;

import java.util.*;

// Arrays의 copyOfRange(원본, 시작인덱스, 마지막인덱스) -> 원본 배열에서 시작인덱스부터 마지막인덱스 -1 까지 복사
public class 모의고사_marked {
    // public int[] solution(int[] array, int[][] commands) {
    // List<Integer> answer = new ArrayList<>();

    // for (int[] c : commands) {
    // int start = c[0] - 1;
    // int end = c[1] - 1;
    // int target = c[2] - 1;
    // List<Integer> arr = new ArrayList<>();

    // for (int i = start; i <= end; i++) {
    // arr.add(array[i]);
    // }

    // int value = arr.stream()
    // .sorted()
    // .skip(target)
    // .findFirst()
    // .orElseThrow();

    // answer.add(value);
    // }
    // return answer.stream()
    // .mapToInt(i -> i.intValue())
    // .toArray();
    // }

    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {
            int[] arr = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
            Arrays.sort(arr);
            answer[i] = arr[commands[i][2] - 1];
        }

        return answer;
    }
}
