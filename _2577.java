import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2577 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int[] count = new int[10];

    int A = Integer.parseInt(br.readLine());
    int B = Integer.parseInt(br.readLine());
    int C = Integer.parseInt(br.readLine());

    int total = A*B*C;

    while(total > 0){
      int digit = total % 10;
      count[digit]++;
      total /= 10;
    }
    for(int i=0; i<count.length; i++){
      System.out.println(count[i]);
    }
  }
}
