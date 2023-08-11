import java.io.*;
import java.util.*;

public class Main {
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        List<Integer[]> home = new ArrayList<>();
        List<Integer[]> chik = new ArrayList<>();
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1)
                    home.add(new Integer[]{i, j});
                else if (map[i][j] == 2)
                    chik.add(new Integer[]{i, j});
            }
        }

        boolean[] open = new boolean[chik.size()];
        solve(0, 0, n, m, home, chik, open);
        System.out.println(res);
    }
   
    public static void solve(int idx, int dep, int n, int m, List<Integer[]> home, List<Integer[]> chik, boolean[] open) {
        if (dep == m) {
            int total = 0;
            for (Integer[] h : home) {
                int min_v = Integer.MAX_VALUE;
                for (int i = 0; i < chik.size(); i++) {
                    if (open[i]) {
                        Integer[] c = chik.get(i);
                        min_v = Math.min(min_v, Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1]));
                    }
                }
                total += min_v;
                if (res <= total)
                    break;
            }
            res = Math.min(res, total);
        }

        for (int i = idx; i < chik.size(); i++) {
            open[i] = true;
            solve(i + 1, dep + 1, n, m, home, chik, open);
            open[i] = false;
        }
    }
}