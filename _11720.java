import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _11720 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int TestCase = Integer.parseInt(br.readLine());
    int Sum=0;
    String Num = br.readLine();

    for(int i=0; i<TestCase; i++){
      char c = Num.charAt(i);
      Sum += ((int)c-48);
    }
    System.out.println(Sum);
  }
}
