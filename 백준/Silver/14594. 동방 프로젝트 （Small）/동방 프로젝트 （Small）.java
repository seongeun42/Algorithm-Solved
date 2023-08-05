import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        boolean[] wall = new boolean[n - 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            for (int j = x - 1; j < y - 1; j++) {
                wall[j] = true;
            }
        }
        int ans = 1;
        for (int i = 0; i < n - 1; i++) {
            if (!wall[i])
                ans++;
        }
        System.out.println(ans);
    }

}