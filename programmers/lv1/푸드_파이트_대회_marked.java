package lv1;

public class 푸드_파이트_대회_marked {
    public String solution(int[] food) {

        String left = "";
        String right = "";

        for (int i = 1; i < food.length; i++) {
            for (int j = 0; j < food[i] / 2; j++) {
                left = left + String.valueOf(i);
                right = String.valueOf(i) + right;
            }
        }
        return left + "0" + right;

    }
}
