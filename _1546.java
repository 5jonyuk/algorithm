import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1546 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    int[] arr = new int[N];

    StringTokenizer st = new StringTokenizer(br.readLine());
    int pos = 0;
    while (st.hasMoreTokens()) {
      arr[pos] = Integer.parseInt(st.nextToken());
      pos++;
    }

    int max = Arrays.stream(arr).max().getAsInt();

    double sum = 0;

    for(int i=0; i<arr.length; i++){
      sum += (double)arr[i]/(double) max * 100;
    }

    double avg = sum / N;

    System.out.println(avg);
  }
}
