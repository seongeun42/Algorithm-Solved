// 줄어들지 않아
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long[][] dp = new long[65][10];
        for (int i = 0; i < 10; i++) {
            dp[0][i] = 1;
        }
        for (int i = 1; i < 65; i++) {
            dp[i][0] = 1;
            for (int j = 1; j < 10; j++){
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            System.out.println(dp[n][9]);
        }
    }
}
