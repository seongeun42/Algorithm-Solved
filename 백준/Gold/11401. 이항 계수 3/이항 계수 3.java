import java.io.*;
import java.util.*;

public class Main {

    static int mod = 1000000007;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        long[] facto = new long[N + 1];
        facto[0] = 1;
        for (int i = 1; i <= N; i++) {
            facto[i] = facto[i - 1] * i % mod;
        }

        long n = facto[N] % mod;
        long r = facto[R] % mod;
        long n_r = facto[N - R] % mod;
        System.out.println(n * fastPow(r * n_r % mod, mod - 2) % mod);
    }

    static long fastPow(long n, int p) {
        if (p == 1)
            return n % mod;
        long v = fastPow(n, p / 2);
        if (p % 2 == 0)
            return v * v % mod;
        return (v * v % mod) * n % mod;
    }

}