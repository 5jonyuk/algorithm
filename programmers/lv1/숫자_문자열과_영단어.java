package lv1;

import java.util.HashMap;
import java.util.Map;

public class 숫자_문자열과_영단어 {
    // public int solution(String s) {
    // String convertAnswer = "";

    // String num = "";
    // for (int i = 0; i < s.length(); i++) {
    // if (Character.isDigit(s.charAt(i))) {
    // convertAnswer = convertAnswer + s.charAt(i);
    // } else {
    // num += s.charAt(i);
    // if (convert(num) != -1) {
    // convertAnswer += String.valueOf(convert(num));
    // num = "";
    // }
    // }
    // }
    // return Integer.valueOf(convertAnswer);
    // }

    // public int convert(String number) {
    // Map<String, Integer> map = new HashMap<>();
    // map.put("zero", 0);
    // map.put("one", 1);
    // map.put("two", 2);
    // map.put("three", 3);
    // map.put("four", 4);
    // map.put("five", 5);
    // map.put("six", 6);
    // map.put("seven", 7);
    // map.put("eight", 8);
    // map.put("nine", 9);

    // return map.getOrDefault(number, -1);
    // }

    public int solution(String s) {

        String[] numWords = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

        for (int i = 0; i < numWords.length; i++) {
            s = s.replaceAll(numWords[i], Integer.toString(i));
        }

        return Integer.parseInt(s);
    }
}
