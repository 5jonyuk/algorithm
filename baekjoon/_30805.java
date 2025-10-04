import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class _30805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        List<Integer> A = new ArrayList<>();
        List<Integer> B = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            B.add(Integer.parseInt(st.nextToken()));
        }

        Set<Integer> Aset = new HashSet<>(A);
        Set<Integer> Bset = new HashSet<>(B);

        List<Integer> result = new ArrayList<>();
        while (true) {
            Set<Integer> Common = Aset.stream()
                    .filter(Bset::contains).collect(Collectors.toSet());
            if (Common.isEmpty()) {
                break;
            }
            int max = Common.stream().max(Integer::compareTo).get();
            result.add(max);
            int i = A.indexOf(max);
            int j = B.indexOf(max);
            A = A.subList(i + 1, A.size());
            B = B.subList(j + 1, B.size());

            Aset = new HashSet<>(A);
            Bset = new HashSet<>(B);
        }
        System.out.println(result.size());
        // for (int x : result) {
        // System.out.print(x + " ");
        // }
        result.forEach(r -> System.out.print(r + " "));
    }
}
