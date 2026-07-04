package lv1;

public class 덧칠하기_marked {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        int maxPainted = section[0] + m - 1;

        for (int i = 1; i < section.length; i++) {
            if (maxPainted < section[i]) {
                answer += 1;
                maxPainted = section[i] + m - 1;
            }
        }
        return answer;
    }
}
