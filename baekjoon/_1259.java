import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1259 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    while(true){
      String testCase = br.readLine();

      StringBuilder sb = new StringBuilder(testCase);
      String outPut = sb.reverse().toString();

      if(testCase.equals("0"))
        break;

      if(outPut.equals(testCase)){
        System.out.println("yes");
      }
      else{
        System.out.println("no");
      }
    }
  }
}
