import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2438 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int length = Integer.parseInt(br.readLine());

    for (int i = 1; i <= length; i++) {
      for (int j = i; j <= length - 1; j++) {
        System.out.print(" ");
      }
      for (int k = 1; k <= i; k++) {
        System.out.print("*");
      }
      System.out.println(" ");
    }
  }
}
