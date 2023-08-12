import java.io.*;
import java.util.*;

public class Main {

    static int readInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = readInt(st), M = readInt(st), H = readInt(st);
        int[] dp = new int[H + 1];
        dp[0] = 1;
        for (int i = 0; i < N; i++) {
            int[] tmp = Arrays.copyOf(dp, H);
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int b = readInt(st);
                for (int h = b; h <= H; h++) {
                    dp[h] += tmp[h - b] % 10007;
                }
            }
        }
        System.out.println(dp[H] % 10007);
    }

}