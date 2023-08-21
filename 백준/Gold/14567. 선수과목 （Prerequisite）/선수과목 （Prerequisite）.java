import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<List<Integer>> G = new ArrayList<>();
        for (int i = 0; i <= N; i++)
            G.add(new ArrayList<>());
        int[] degree = new int[N + 1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            G.get(A).add(B);
            degree[B]++;
        }

        int[] ans = new int[N];
        Deque<int[]> q = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            if (degree[i] == 0) {
                ans[i - 1] = 1;
                q.add(new int[] {i, 1});
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.pollFirst();
            for (int nn : G.get(cur[0])) {
                degree[nn]--;
                if (degree[nn] == 0) {
                    ans[nn - 1] = cur[1] + 1;
                    q.add(new int[] {nn, cur[1] + 1});
                }
            }
        }

        for (int i = 0; i < N; i++)
            sb.append(ans[i]).append(" ");
        System.out.println(sb);
    }

}