package lv1;

import java.util.*;

// 먼저 lost와 reserve 정렬
// lost를 돌면서 2, 3번을 한 번에 하지말고 분리
public class 체육복_marked {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        boolean[] isParticipation = new boolean[n];

        Arrays.fill(isParticipation, true);
        Arrays.sort(lost);
        Arrays.sort(reserve);

        // 1. 잃어버린 애들 false 처리
        for (int l : lost) {
            isParticipation[l - 1] = false;
        }

        // 2. 여벌옷이 있지만 잃어버린 애들 처리
        for (int i = 0; i < lost.length; i++) {
            if (isReserveAndLost(lost[i], reserve)) {
                isParticipation[lost[i] - 1] = true;
            }
        }

        // 3. 빌리기 작업
        for (int i = 0; i < lost.length; i++) {
            if (isBorrow(lost[i], reserve)) {
                isParticipation[lost[i] - 1] = true;
            }
        }

        // 4. 참여할 수 있는 애들 계산
        for (int i = 0; i < isParticipation.length; i++) {
            if (isParticipation[i]) {
                answer++;
            }
        }
        return answer;
    }

    public boolean isReserveAndLost(int lost, int[] reserve) {
        for (int j = 0; j < reserve.length; j++) {
            if (reserve[j] == lost) {
                reserve[j] = -99;
                return true;
            }
        }
        return false;
    }

    public boolean isBorrow(int lost, int[] reserve) {
        // 왼쪽에서 먼저 빌리기
        for (int j = 0; j < reserve.length; j++) {
            if (reserve[j] == lost - 1) {
                reserve[j] = -99;
                return true;
            }
            if (reserve[j] == lost + 1) {
                reserve[j] = -99;
                return true;
            }
        }
        return false;
    }
}
