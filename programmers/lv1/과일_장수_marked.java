package lv1;

import java.util.*;

public class 과일_장수_marked {
    // public int solution(int k, int m, int[] score) {

    // // score의 길이동안 score가 k보다 작다면 제거(-1)
    // for (int i = 0; i < score.length; i++) {
    // if (score[i] > k) {
    // score[i] = -1;
    // }
    // }

    // // 내림차순 정렬
    // int[] sortedArrays = Arrays.stream(score)
    // .boxed()
    // .sorted(Comparator.reverseOrder())
    // .mapToInt(Integer::intValue)
    // .toArray();

    // // m개 묶기
    // int profit = 0;
    // for (int i = 0; i < sortedArrays.length; i += m) {
    // boolean stop = false;
    // int minValue = 0;
    // for (int j = i; j < i + m; j++) {
    // if (j >= score.length || sortedArrays[j] == -1) {
    // stop = true;
    // break;
    // }
    // minValue = sortedArrays[j];
    // }
    // if (stop) {
    // break;
    // }
    // // profit += 가장 최저 점수 * m
    // profit += (minValue * m);
    // }

    // return profit;
    // }

    public int solution(int k, int m, int[] score) {
        int profit = 0;

        Arrays.sort(score);

        for (int i = score.length; i >= m; i -= m) {
            profit += score[i - m] * m;
        }

        return profit;
    }
}
