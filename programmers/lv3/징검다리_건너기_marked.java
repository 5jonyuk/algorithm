package lv3;

import java.util.*;

public class 징검다리_건너기_marked {
    private boolean check(int[] stones, int mid, int k) {
        int count = 0;
        for (int i = 0; i < stones.length; i++) {
            if (stones[i] < mid) {
                count++;
                if (count >= k) {
                    return false;
                }
            } else {
                count = 0;
            }
        }

        return true;
    }

    public int solution(int[] stones, int k) {
        int answer = 0;

        int low = Arrays.stream(stones).min().getAsInt();
        int high = Arrays.stream(stones).max().getAsInt();

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (check(stones, mid, k)) {
                answer = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return answer;
    }
}
