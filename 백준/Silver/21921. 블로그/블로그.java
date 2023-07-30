import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int[] cnt = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cnt[i] = Integer.parseInt(st.nextToken());
        }

        int[] ans = new int[2];
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += cnt[i];
            if (i >= X - 1) {
                if (i >= X) {
                    sum -= cnt[i - X];
                }
                if (ans[0] < sum) {
                    ans[0] = sum;
                    ans[1] = 1;
                } else if (ans[0] == sum) {
                    ++ans[1];
                }
            }
        }

        if (ans[0] == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(ans[0] + "\n" + ans[1]);
        }
    }
}