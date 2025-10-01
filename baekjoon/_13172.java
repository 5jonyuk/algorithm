import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

// BigInteger는 산술연산 불가

// int vs Integer
/*
int
- 타입: 원시타입
- null허용: x
- 메서드: x
- 컬렉션 사용: x
- 속도: 빠름

Integer
- 타입: 객체(참조 타입)
- null허용: o
- 메서드: o (toString, parseInt 등)
- 컬렉션 사용: o
- 속도: 상대적으로 느림
*/
public class _13172 {
    static BigInteger X = BigInteger.valueOf(1000000007L);

    public static BigInteger getNValue(BigInteger n, BigInteger exp) {
        if (exp.equals(BigInteger.valueOf(1))) {
            return n;
        }
        if (exp.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO)) {
            BigInteger half = getNValue(n, exp.divide(BigInteger.valueOf(2)));
            return half.multiply(half).mod(X);
        } else {
            return n.multiply(getNValue(n, exp.subtract(BigInteger.valueOf(1)))).mod(X);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        Integer m = Integer.parseInt(br.readLine());
        BigInteger total = BigInteger.ZERO;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            BigInteger N = new BigInteger(st.nextToken());
            BigInteger S = new BigInteger(st.nextToken());
            BigInteger g = N.gcd(S);
            N = N.divide(g);
            S = S.divide(g);

            total = total.add(S.multiply(getNValue(N, X.subtract(BigInteger.valueOf(2)))));
            total = total.mod(X);
        }
        System.out.println(total);
    }
}
