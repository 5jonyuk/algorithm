import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class _14502 {
    public static int n, m;
    public static int[][] labs;
    public static List<int[]> blank = new ArrayList<>();
    public static List<int[]> virus = new ArrayList<>();
    // 선언과 동시에 초기화 할 때는 new 생략가능
    public static int[] dx = { 1, -1, 0, 0 };
    // 컴파일러가 자동으로 아래와 같이 바꿔줌
    public static int[] dy = new int[] { 0, 0, -1, 1 };
    public static int max_safe = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        labs = new int[n][m];

        for (int i = 0; i < n; i++) {
            /*
             * br.readLine()으로 입력의 한 줄(예: "0 1 2 0 0")을 문자열로 읽어옴.
             * StringTokenizer는 기본적으로 공백(스페이스, 탭 등)을 기준으로 문자열을 토큰(단어)으로 나눔.
             * st는 이 줄의 토큰들을 순서대로 꺼낼 수 있는 도구가 됩니다.
             */
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                /*
                 * st.nextToken()이 줄의 다음 토큰(예: "0", "1")을 문자열로 반환.
                 * Integer.parseInt(...)로 문자열을 정수로 변환해서 labs[i][j]에 저장.
                 */
                labs[i][j] = Integer.parseInt(st.nextToken());
                if (labs[i][j] == 0) {
                    // 메소드 호출인자로 배열을 생성할 때는 무조건 new 필요
                    blank.add(new int[] { i, j });
                } else if (labs[i][j] == 2) {
                    virus.add(new int[] { i, j });
                }
            }
        }
        makeWall(0, 0, new int[3][]);
        System.out.println(max_safe);
    }

    public static void makeWall(int start, int depth, int[][] walls) {
        if (depth == 3) {
            // 1. 카피
            int[][] tempLabs = copyLabs();
            // 2. 벽세우기
            for (int[] w : walls) {
                tempLabs[w[0]][w[1]] = 1;
            }
            // 3. 바이러스퍼뜨리기
            bfs(tempLabs);
            // 4. 안전구역 세기
            int safe = countSafe(tempLabs);
            max_safe = Math.max(safe, max_safe);
            // 5. 리턴
            return;
        }
        for (int i = start; i < blank.size(); i++) {
            walls[depth] = blank.get(i);
            makeWall(i + 1, depth + 1, walls);
        }
    }

    // Queue<int[]> q = new LinkedList<>();
    // Queue<int[]> q = new ArrayDeque<>();
    /*
     * LinkedList는 Queue 인터페이스의 구현체
     * LinkedList안에 덱, 큐, 리스트 기능 다 존재
     * 그 기능 중 큐 기능만 쓰려고 변수를 큐로 제한
     * 제한하는 이유
     * 가독성, 유연한 구현체 교체, 인터페이스 지향 프로그래밍 원칙
     */
    public static void bfs(int[][] tempLabs) {
        Queue<int[]> q = new LinkedList<>();
        for (int[] v : virus) {
            q.add(v);
        }
        while (!q.isEmpty()) {
            int cur[] = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (tempLabs[nx][ny] == 0) {
                        tempLabs[nx][ny] = 2;
                        q.add(new int[] { nx, ny });
                    }
                }
            }

        }
    }

    public static int countSafe(int[][] tempLabs) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tempLabs[i][j] == 0) {
                    count++;
                }
            }
        }
        return count;
    }

    public static int[][] copyLabs() {
        int[][] newLab = new int[n][m];
        for (int i = 0; i < n; i++) {
            newLab[i] = labs[i].clone();
        }
        return newLab;
    }
}
