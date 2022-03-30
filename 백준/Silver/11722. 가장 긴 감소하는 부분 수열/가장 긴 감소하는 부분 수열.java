import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int[] dp = new int[n];
        int res = Integer.MIN_VALUE;
        String[] str = br.readLine().split(" ");
        for (int i = 0; i < n; i++)
            a[i] = Integer.parseInt(str[i]);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (a[i] < a[j])
                    dp[i] = Math.max(dp[i], dp[j]);
            }
            dp[i] += 1;
            res = Math.max(res, dp[i]);
        }

        System.out.println(res);
    }
}