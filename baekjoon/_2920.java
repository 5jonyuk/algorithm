import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2920 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int[] recode  = new int[8];

    for(int i=0; i<recode.length; i++){
      recode[i] = Integer.parseInt(st.nextToken());
    }

    boolean ascending = true;
    boolean descending = true;

    for(int i=0; i<recode.length-1; i++){
      if(recode[i] < recode[i+1]) {
        descending = false;
      }
      else if (recode[i] > recode[i+1]){
        ascending = false;
      }
    }
   if(ascending) System.out.println("ascending");
   else if(descending) System.out.println("descending");
   else System.out.println("mixed");
  }
}
