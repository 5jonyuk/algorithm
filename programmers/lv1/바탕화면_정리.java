package lv1;

public class 바탕화면_정리 {
    //    public int[] solution(String[] wallpaper) {
//        int start_x = 9999;
//        int start_y = 9999;
//        int end_x = 0;
//        int end_y = 0;
//
//        char[][] desktop = new char[wallpaper.length][wallpaper[0].length()];
//        for (int i = 0; i < wallpaper.length; i++) {
//            for (int j = 0; j < wallpaper[0].length(); j++) {
//                desktop[i][j] = wallpaper[i].charAt(j);
//            }
//        }
//
//        for (int i = 0; i < desktop.length; i++) {
//            for (int j = 0; j < desktop[i].length; j++) {
//                if (desktop[i][j] == '#') {
//                    if (start_x > i) {
//                        start_x = i;
//                    }
//                    if (start_y > j) {
//                        start_y = j;
//                    }
//                    if (end_x < i) {
//                        end_x = i;
//                    }
//                    if (end_y < j) {
//                        end_y = j;
//                    }
//                }
//            }
//        }
//        return new int[]{start_x, start_y, end_x+1, end_y+1};
//    }
    public int[] solution(String[] wallpaper) {
        int start_x = Integer.MAX_VALUE;
        int start_y = Integer.MAX_VALUE;
        int end_x = Integer.MIN_VALUE;
        int end_y = Integer.MIN_VALUE;

        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[0].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    start_x = Math.min(start_x, i);
                    start_y = Math.min(start_y, j);
                    end_x = Math.max(end_x, i);
                    end_y = Math.max(end_y, j);
                }
            }
        }
        return new int[]{start_x, start_y, end_x + 1, end_y + 1};
    }
}
