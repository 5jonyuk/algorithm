import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2475 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int[] num = new int[5];
    int sum = 0;
    for(int i=0; i<num.length; i++){
      num[i] = Integer.parseInt(st.nextToken());
      sum += (int)Math.pow(num[i],2);
    }
    System.out.println(sum%10);
  }
}
