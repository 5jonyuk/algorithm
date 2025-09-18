import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class _1676 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int num = Integer.parseInt(br.readLine());
    int count = 0;
    for (int i = 1; i <= num; i++) {
      if (i % 5 == 0) {
        int temp = i;
        while (temp % 5 == 0) {
          count++;
          temp /= 5;
        }
      }
    }
    System.out.println(count);
  }
}