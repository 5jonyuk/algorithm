import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class _3052 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    HashSet<Integer> Number = new HashSet<Integer>();

    for(int i=0; i<10; i++){
      Number.add(Integer.parseInt(br.readLine())%42);
    }
    System.out.println(Number.size());
  }
}