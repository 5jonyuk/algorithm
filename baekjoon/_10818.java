import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10818 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int TestCase = Integer.parseInt(br.readLine());
    int[] num = new int[TestCase];

    StringTokenizer st = new StringTokenizer(br.readLine());
    for(int i=0; i<TestCase; i++){
      num[i]=Integer.parseInt(st.nextToken());
    }

    int MinNum, MaxNum;
    MaxNum=MinNum=num[0];

    for(int i=0; i<TestCase; i++){
      if(MinNum>num[i])
        MinNum = num[i];
      if(num[i]>MaxNum)
        MaxNum=num[i];
    }
    System.out.print(MinNum+" "+MaxNum);
  }
}
