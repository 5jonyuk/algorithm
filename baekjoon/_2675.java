import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2675 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    StringBuilder result = new StringBuilder();

    for(int k=0; k<T; k++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int R = Integer.parseInt(st.nextToken());
      String S = st.nextToken();

      if (isT(T) && isR(R) && isS(S)) {
          for (int j = 0; j < S.length(); j++) {
            char p = S.charAt(j);
            for(int z=0; z<R; z++){
              result.append(p);
            }
        }
        result.append("\n");
      }
    }
    System.out.println(result.toString());
  }
  static boolean isT(int T){
    return T>=1 && T<=1000;
  }
  static boolean isR(int R){
    return R>=1 && R<=8;
  }
  static boolean isS(String S){
    return S.length()>=1 && S.length()<=20;
  }
}