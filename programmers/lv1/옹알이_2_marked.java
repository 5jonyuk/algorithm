package lv1;

public class 옹알이_2_marked {
    public int solution(String[] babbling) {
        int answer = 0;

        for (int i = 0; i < babbling.length; i++) {
            String str = babbling[i];

            if (str.contains("ayaaya") || str.contains("yeye") || str.contains("woowoo") || str.contains("mama")) {
                continue;
            }
            str = str.replaceAll("aya", " ");
            str = str.replaceAll("ye", " ");
            str = str.replaceAll("woo", " ");
            str = str.replaceAll("ma", " ");

            str = str.replaceAll(" ", "");
            if (str.length() == 0) {
                answer++;
            }

        }
        return answer;
    }
}
