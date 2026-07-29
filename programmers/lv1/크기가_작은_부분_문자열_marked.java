package lv1;
// p는 최대 18자리까지 가능

// int는 21억(10자리 숫자)만 커버 가능 
// double은 부동소수점 오차(정밀도 손실)
// double도 매우 큰 수를 표현할 수 있지만 15~17자리를 넘어가면 정확한 정수 값을 보장하지 못하고 오차(반올림/정밀도 손실)가 발생함.

public class 크기가_작은_부분_문자열_marked {
    public int solution(String t, String p) {
        int answer = 0;
        long stdNumber = Long.valueOf(p);

        for (int i = 0; i < t.length() - p.length() + 1; i++) {
            long targetNumber = Long.valueOf(t.substring(i, i + p.length()));
            if (targetNumber <= stdNumber) {
                answer++;
            }
        }

        return answer;
    }
}
