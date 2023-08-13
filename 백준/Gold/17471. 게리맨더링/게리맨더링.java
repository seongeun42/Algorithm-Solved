import java.io.*;
import java.util.*;

public class Main {

    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = readInt(br.readLine());
        int[] population = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            population[i] = readInt(st.nextToken());
        }

        int one = 0;
        List<List<Integer>> G = new ArrayList<>();
        G.add(new ArrayList<>());
        for (int i = 1; i <= N; i++) {
            G.add(new ArrayList<>());
            st = new StringTokenizer(br.readLine());
            int cnt = readInt(st.nextToken());
            if (cnt == 0) one++;
            for (int j = 0; j < cnt; j++) {
                G.get(i).add(readInt(st.nextToken()));
            }
        }

        if (N > 2 && one > 1)
            System.out.println(-1);
        else if (one == 1) {
            ans = 0;
            for (int i = 1; i <= N; i++) {
                ans += G.get(i).isEmpty() ? -population[i] : population[i];
            }
            System.out.println(Math.abs(ans));
        }
        else {
            boolean[] pick = new boolean[N + 1];
            for (int i = 1; i <= N / 2; i++) {
                dfs(i, 0, 1, pick, G, population);
            }
            System.out.println(ans != Integer.MAX_VALUE ? ans : -1);
        }
    }

    static void dfs(int cnt, int dep, int idx, boolean[] pick, List<List<Integer>> G, int[] population) {
        if (dep == cnt) {
            int a = -1, b = -1;
            for (int i = 1; i < pick.length; i++) {
                if (a != -1 && b != -1) break;
                if (a == -1 && pick[i]) {
                    a = bfs(pick, G, i, true);
                }
                if (b == -1 && !pick[i]) {
                    b = bfs(pick, G, i, false);
                }
            }
            if (a + b == pick.length - 1) {
                int res = 0;
                for (int i = 1; i < pick.length; i++) {
                    res += pick[i] ? population[i] : -population[i];
                }
                res = Math.abs(res);
                if (ans > res)
                    ans = res;
            }
            return;
        }

        for (int i = idx; i < pick.length; i++) {
            pick[i] = true;
            dfs(cnt, dep + 1, i + 1, pick, G, population);
            pick[i] = false;
        }
    }

    static int bfs(boolean[] pick, List<List<Integer>> G, int start, boolean team) {
        Deque<Integer> q = new ArrayDeque<>();
        q.addLast(start);
        boolean[] visited = new boolean[pick.length];
        visited[start] = true;
        int cnt = 0;
        while (!(q.isEmpty())) {
            int cn = q.pollFirst();
            cnt++;
            for (int nn : G.get(cn)) {
                if (!visited[nn] && pick[nn] == team) {
                    visited[nn] = true;
                    q.addLast(nn);
                }
            }
        }
        return cnt;
    }
    
    static int readInt(String str) { return Integer.parseInt(str); }

}