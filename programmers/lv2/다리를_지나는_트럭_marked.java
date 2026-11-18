package lv2;

import java.util.*;

public class 다리를_지나는_트럭_marked {
    class Solution {
        public int solution(int bridge_length, int weight, int[] truck_weights) {
            Deque<Integer> q = new ArrayDeque<>();
            for (int i = 0; i < bridge_length; i++) {
                q.addLast(0);
            }

            int time = 0;
            int currentSum = 0;
            int idx = 0;

            while (idx < truck_weights.length) {
                int out = q.pollFirst();
                currentSum -= out;

                int tw = truck_weights[idx];

                if (currentSum + tw <= weight) {
                    q.addLast(tw);
                    currentSum += tw;
                    idx++;
                } else {
                    q.addLast(0);
                }

                time++;

            }
            return time + bridge_length;
        }
    }
}
