import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        boolean[] live = new boolean[n + 1];
        for (int i = 0; i < q; i++) {
            int x = Integer.parseInt(br.readLine());
            int u = x;
            int res = live[x] ? x : 0;
            while (u != 1) {
                u >>= 1;
                if (live[u])
                    res = u;
            }
            if (res == 0)
                live[x] = true;
            sb.append(res).append("\n");
        }
        System.out.println(sb);
    }

}