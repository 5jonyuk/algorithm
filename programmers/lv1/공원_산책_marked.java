package lv1;

public class 공원_산책_marked {
    int start_x = 0;
    int start_y = 0;

    public int[] solution(String[] park, String[] routes) {
        char[][] map = new char[park.length][park[0].length()];

        for (int i = 0; i < park.length; i++) {
            String str = park[i];
            for (int j = 0; j < str.length(); j++) {
                map[i][j] = str.charAt(j);
                if (str.charAt(j) == 'S') {
                    start_x = i;
                    start_y = j;
                }
            }
        }

        for (String op : routes) {
            String[] cmd = op.split(" ");
            if (check(cmd[0], Integer.parseInt(cmd[1]), map)) {
                move(cmd[0], Integer.parseInt(cmd[1]));
            }
        }

        return new int[]{start_x, start_y};
    }

    private boolean check(String direction, int value, char[][] map) {
        int dx = 0;
        int dy = 0;

        switch (direction) {
            case "E" -> dy = 1;
            case "W" -> dy = -1;
            case "S" -> dx = 1;
            case "N" -> dx = -1;
        }

        for (int i = 1; i <= value; i++) {
            int nx = start_x + dx * i;
            int ny = start_y + dy * i;

            if (nx < 0 || nx > map.length - 1 || ny < 0 || ny > map[0].length - 1) {
                return false;
            }

            if (map[nx][ny] == 'X') {
                return false;
            }
        }
        return true;
    }

    private void move(String direction, int value) {
        if (direction.equals("E")) {
            start_y += value;
        }

        if (direction.equals("W")) {
            start_y -= value;
        }

        if (direction.equals("S")) {
            start_x += value;
        }

        if (direction.equals("N")) {
            start_x -= value;
        }
    }
}
