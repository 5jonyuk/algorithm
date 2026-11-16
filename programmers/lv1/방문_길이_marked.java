package lv1;

import java.util.*;

class Solution {
    record Point(int x, int y) {
    }

    record Path(Point from, Point to) {
    }

    public int solution(String dirs) {
        int answer = 0;

        int[] dx = { -1, 1, 0, 0 };
        int[] dy = { 0, 0, -1, 1 };
        int x = 0;
        int y = 0;

        Map<Character, Integer> map = new HashMap<>();
        map.put('U', 0);
        map.put('D', 1);
        map.put('L', 2);
        map.put('R', 3);

        Set<Path> visited = new HashSet<>();

        for (int i = 0; i < dirs.length(); i++) {
            int d = map.get(dirs.charAt(i));
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx >= -5 && nx <= 5 && ny <= 5 && ny >= -5) {
                Path path = new Path(new Point(x, y), new Point(nx, ny));
                Path reversePath = new Path(new Point(nx, ny), new Point(x, y));
                x = nx;
                y = ny;

                if (!visited.contains(path) && !visited.contains(reversePath)) {
                    visited.add(path);
                    visited.add(reversePath);
                    answer++;
                }
            }
        }
        return answer;
    }
}