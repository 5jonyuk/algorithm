package lv1;

import java.util.*;

public class 명예의_전당1_marked {
    // public int[] solution(int k, int[] score) {
    // List<Integer> anwer = new ArrayList<>();
    // List<Integer> hallOfFame = new ArrayList<>();

    // for (int i = 0; i < score.length; i++) {
    // hallOfFame.add(score[i]);
    // hallOfFame = hallOfFame.stream()
    // .sorted(Comparator.reverseOrder())
    // .limit(k)
    // // .toList(); 불변 리스트 반환 때문에 안됨
    // .collect(Collectors.toList());
    // anwer.add(hallOfFame.get(hallOfFame.size() - 1));
    // }

    // return anwer.stream()
    // .mapToInt(Integer::intValue)
    // .toArray();
    // }

    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> pq = new PriorityQueue<>(); // 오름차순 최소 힙

        for (int i = 0; i < score.length; i++) {
            pq.add(score[i]);

            if (pq.size() > k) {
                pq.poll(); // 가장 작은 수 제거
            }

            answer[i] = pq.peek(); // 0번째 수 읽기만
        }

        return answer;
    }
}
