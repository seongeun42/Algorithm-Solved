import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int M = Integer.parseInt(br.readLine());
            int[] dp = new int[M + 1];
            while (N-- > 0) {
                int c = Integer.parseInt(st.nextToken());
                if (c > M) break;
                dp[c] += 1;
                for (int m = c + 1; m <= M; m++) {
                    dp[m] += dp[m - c];
                }
            }
            sb.append(dp[M]).append("\n");
        }
        System.out.println(sb);
    }

}