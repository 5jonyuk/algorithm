package lv1;

public class 문자열_나누기_marked {
    // public int solution(String s) {
    // int answer = 0;
    // int standardCnt = 0;
    // int targetCnt = 0;

    // while (s.length() > 0) {
    // if (s.length() == 1) {
    // answer++;
    // break;
    // }

    // char standardChar = s.charAt(0);
    // standardCnt++;

    // for (int i = 1; i < s.length(); i++) {
    // char targetChar = s.charAt(i);

    // if (standardChar == targetChar) {
    // standardCnt++;
    // } else {
    // targetCnt++;
    // if (standardCnt == targetCnt) {
    // String extractedString = s.substring(0, i + 1);
    // answer++;
    // s = s.replaceFirst(extractedString, "");
    // break;
    // }
    // }
    // }
    // }

    // return answer;
    // }

    public int solution(String s) {
        int answer = 0;
        int standardCnt = 0;
        int targetCnt = 0;
        char standardChar = ' ';

        for (int i = 0; i < s.length(); i++) {
            if (standardCnt == 0) {
                standardChar = s.charAt(i);
                standardCnt = 1;
                answer++;
                continue;
            }

            if (s.charAt(i) == standardChar) {
                standardCnt++;
            } else {
                targetCnt++;
            }

            if (standardCnt == targetCnt) {
                standardCnt = 0;
                targetCnt = 0;
            }
        }

        return answer;
    }
}
