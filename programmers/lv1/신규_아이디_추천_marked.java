package lv1;

public class 신규_아이디_추천_marked {
    public String solution(String new_id) {
        String answer = "";

        // 1단계
        answer = new_id.toLowerCase();

        // 2단계
        answer = answer.replaceAll("[^a-z0-9._-]", "");

        // 3단계
        answer = answer.replaceAll("\\.{2,}", ".");

        // 4단계
        // if (answer.startsWith(".")) {
        // answer = answer.substring(1);
        // }

        // if (answer.endsWith(".")) {
        // answer = answer.substring(0, answer.length() - 1);
        // }
        answer = answer.replaceAll("^[.]|[.]$", "");

        // 5단계
        if (answer.isBlank()) {
            answer = "a";
        }

        // 6단계
        if (answer.length() >= 16) {
            answer = answer.substring(0, 15);
            // if (answer.charAt(answer.length() - 1) == '.') {
            // answer = answer.substring(0, answer.length() - 1);
            // }
            answer = answer.replaceAll("[.]$", "");
        }

        // 7단계
        if (answer.length() <= 2) {
            while (answer.length() != 3) {
                answer += answer.charAt(answer.length() - 1);
            }
        }

        return answer;
    }
}
