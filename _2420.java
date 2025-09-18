import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2420 {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        Long n = Long.parseLong(stringTokenizer.nextToken());
        Long m = Long.parseLong(stringTokenizer.nextToken());

        System.out.println(Math.abs(n-m));
    }
}