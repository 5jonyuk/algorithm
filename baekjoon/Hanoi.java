import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Hanoi {
    public static void hanoi_tower(int n, char start, char mid, char end) {
        if (n == 1) System.out.printf("원판 1을 %c 에서 %c으로 옮긴다.\n", start, end);
        else {
            hanoi_tower(n - 1, start, end, mid);
            System.out.printf("원판 %d을 %c에서 %c으로 옮긴다.\n", n, start, end);
            hanoi_tower(n - 1, mid, start, end);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        hanoi_tower(3,'A','B','C');
    }
}
