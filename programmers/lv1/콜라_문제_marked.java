package lv1;

public class 콜라_문제_marked {
    public int solution(int a, int b, int n) {
        int answer = 0;

        while (n >= a) {
            int newCoke = n / a * b;
            int remaining = n % a;

            answer += newCoke;
            n = newCoke + remaining;
        }
        return answer;
    }
}
