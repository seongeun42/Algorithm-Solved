import java.io.*;
import java.util.*;

public class Main {

    static boolean[] alpa = new boolean[26];
    static String[] map;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int R, C, ans;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        map = new String[R];
        for (int i = 0; i < R; i++) {
            map[i] = br.readLine();
        }
        dfs(0, 0, 1);
        System.out.println(ans);
    }

    static void dfs(int cx, int cy, int cnt) {
        if (cnt > 26) return;
        if (ans < cnt)
            ans = cnt;
        alpa[map[cy].charAt(cx) - 'A'] = true;
        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i], ny = cy + dy[i];
            if (0 <= nx && nx < C && 0 <= ny && ny < R) {
                int idx = map[ny].charAt(nx) - 'A';
                if (!alpa[idx]) {
                    dfs(nx, ny, cnt + 1);
                    alpa[idx] = false;
                }
            }
        }
    }

}