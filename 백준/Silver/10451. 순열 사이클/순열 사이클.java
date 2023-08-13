import java.io.*;
import java.util.*;

public class Main {

    static int readInt(String str) { return Integer.parseInt(str); }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = readInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            int n = readInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] num = new int[n];
            for (int i = 0; i < n; i++) {
                num[i] = readInt(st.nextToken());
            }
            int ans = 0;
            int[] chk = new int[n];
            for (int i = 0; i < n; i++) {
                if (chk[i] == 0) {
                    ans += cycle(num, chk, i, i + 1);
                }
            }
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static int cycle(int[] num, int[] chk, int idx, int c) {
        if (chk[idx] != 0) {
            return chk[idx] == c ? 1 : 0;
        }
        chk[idx] = c;
        return cycle(num, chk, num[idx] - 1, c);
    }

}