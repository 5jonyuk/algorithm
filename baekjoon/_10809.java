import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

public class _10809 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int[] alphabet = new int[26];

    Arrays.fill(alphabet, -1);
    for (int i=0; i < str.length(); i++) {
      char c = str.charAt(i);
      if(alphabet[c-'a']==-1) {
        alphabet[c-'a']=i;
      }
    }
    for(int i:alphabet) {
      System.out.print(i + " ");
    }
  }
}
