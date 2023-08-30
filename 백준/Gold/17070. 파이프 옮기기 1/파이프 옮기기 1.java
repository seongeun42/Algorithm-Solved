import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[][] map = new String[N][N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().split(" ");
        }

        int[][][] dp = new int[N + 1][N][3];
        dp[0][1][0] = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 2; j < N; j++) {
                if (map[i][j].equals("1"))
                    continue;
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2];
                if (i > 0)
                    dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2];
                if (i > 0 && !map[i - 1][j].equals("1") && !map[i][j - 1].equals("1"))
                    dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2];
            }
        }
        System.out.println(dp[N - 1][N - 1][0] + dp[N - 1][N - 1][1] + dp[N - 1][N - 1][2]);
    }

}