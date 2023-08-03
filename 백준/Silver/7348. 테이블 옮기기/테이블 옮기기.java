import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int tc = Integer.parseInt(br.readLine());
        while (tc-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] aisle = new int[200];
            while (n-- > 0) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int t = Integer.parseInt(st.nextToken());
                if (s % 2 == 1) ++s;
                if (t % 2 == 1) ++t;
                int start = Math.min(s, t) / 2 - 1;
                int end = Math.abs(s - t) / 2 + start;
                for (int i = start; i <= end; i++) {
                    ++aisle[i];
                }
            }
            int ans = 0;
            for (int i = 0; i < 200; i++) {
                if (ans < aisle[i])
                    ans = aisle[i];
            }
            sb.append(ans * 10).append("\n");
        }
        System.out.println(sb);
    }

}