import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10952 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    String input;

    while((input=br.readLine())!=null){
      st = new StringTokenizer(input);

      int A = Integer.parseInt(st.nextToken());
      int B = Integer.parseInt(st.nextToken());

      if(A==0 && B==0) break;
      int Sum = A+B;

      System.out.println(Sum);
    }
    br.close();
  }
}