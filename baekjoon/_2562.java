import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2562 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int[] num = new int[9];

    for(int i=0; i<num.length; i++){
      if(num[i]<100)
        num[i]=Integer.parseInt(br.readLine());
      else System.out.println("100이하 숫자를 입력하시오");
    }
    int maxNum = num[0];
    int maxIndex = 0;
    for(int i=1; i<num.length; i++){
      if(maxNum<num[i]){
        maxNum = num[i];
        maxIndex = i;
      }
    }
    System.out.println(maxNum);
    System.out.println(maxIndex+1);
  }
}
