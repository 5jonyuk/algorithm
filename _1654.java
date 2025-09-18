import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class _1654{
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int K = Integer.parseInt(st.nextToken());
    int N = Integer.parseInt(st.nextToken());

    int[] arr = new int[K];
    long max = 0;

    for (int i = 0; i < arr.length; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    max = Arrays.stream(arr).max().getAsInt();

    long start = 0;
    long end = max;
    end++;

    while (start < end) {
      long mid = (start + end) / 2;

      long sum = 0;
      for (int i = 0; i < arr.length; i++) {
        sum += (arr[i] / mid);
      }

      if (sum < N) {
        end = mid;
      } else {
        start = mid + 1;
      }
    }
    System.out.println(start - 1);
  }
}
