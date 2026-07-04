package lv1;

public class 대충_만든_자판_marked {
    public int find(String[] keymap, char c) {
        int minIndex = Integer.MAX_VALUE;
        for (String str : keymap) {
            if (str.indexOf(c) == -1) {
                continue;
            }
            minIndex = Integer.min(str.indexOf(c), minIndex);
        }

        if (minIndex == Integer.MAX_VALUE) {
            return -1;
        }
        return minIndex + 1;
    }

    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        int index = 0;

        for (String str : targets) {
            int sum = 0;
            boolean isPossible = true;

            for (int i = 0; i < str.length(); i++) {
                int findNum = find(keymap, str.charAt(i));
                if (findNum == -1) {
                    isPossible = false;
                    break;
                }
                sum += findNum;
            }

            if (isPossible) {
                answer[index++] = sum;
            } else {
                answer[index++] = -1;
            }
        }

        return answer;
    }
}
