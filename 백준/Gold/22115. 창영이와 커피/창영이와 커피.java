import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] dp = new int[K + 1];
        Arrays.fill(dp, 101);
        dp[0] = 0;
        st = new StringTokenizer(br.readLine());
        int c, all = 0;
        for (int i = 0; i < N; i++) {
            c = Integer.parseInt(st.nextToken());
            for (int k = Math.min(all + c, K); k >= c; k--) {
                if (dp[k] > dp[k - c] + 1)
                    dp[k] = dp[k - c] + 1;
            }
            all += c;
        }
        System.out.println(dp[K] == 101 ? -1 : dp[K]);
    }

}