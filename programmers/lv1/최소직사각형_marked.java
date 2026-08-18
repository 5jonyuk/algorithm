package lv1;

public class 최소직사각형_marked {
    public void swap(int[][] arr, int i) {
        int temp = arr[i][0];
        arr[i][0] = arr[i][1];
        arr[i][1] = temp;
    }

    public int solution(int[][] sizes) {
        int answer_width = 0;
        int answer_height = 0;

        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] < sizes[i][1]) {
                swap(sizes, i);
            }
            answer_width = Math.max(answer_width, sizes[i][0]);
            answer_height = Math.max(answer_height, sizes[i][1]);
        }

        return answer_width * answer_height;
    }
}
