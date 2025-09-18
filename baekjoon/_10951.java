import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10951 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    String input;

    while((input=br.readLine())!=null){
      st = new StringTokenizer(input);

      int A = Integer.parseInt(st.nextToken());
      int B = Integer.parseInt(st.nextToken());
      int Sum = A+B;

      System.out.println(Sum);
    }
    br.close();
  }
}
