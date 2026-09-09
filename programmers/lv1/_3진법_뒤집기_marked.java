package lv1;

// import java.util.*;

public class _3진법_뒤집기_marked {
    // public int solution(int n) {
    // int answer = 0;
    // List<Integer> arr = new ArrayList<>();

    // // 10진수 -> 3진수로 변환
    // while (n > 0) {
    // arr.add(n % 3);
    // n /= 3;
    // }

    // // 계산
    // for (int j = 0; j < arr.size(); j++) {
    // answer += arr.get(j) * Math.pow(3.0, arr.size() - j - 1);
    // }
    // return answer;
    // }

    public int solution(int n) {
        String answer = "";

        while (n > 0) {
            answer = answer + (n % 3);
            n /= 3;
        }

        return Integer.parseInt(answer, 3);
    }
}
