import java.io.*;
import java.util.*;

public class Main {

    static int readInt(StringTokenizer st) { return Integer.parseInt(st.nextToken()); }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            int R = readInt(st), C = readInt(st);
            int[] root = new int[R * C];
            for (int i = 0; i < R * C; i++) {
                root[i] = i;
            }
            int[][] E = new int[(R - 1) * C + R * (C - 1)][3];
            int cnt = 0;
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C - 1; j++) {
                    int n = i * C + j;
                    E[cnt++] = new int[] { readInt(st), n, n + 1 };
                }
            }
            for (int i = 0; i < R - 1; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    int n = i * C + j;
                    E[cnt++] = new int[] { readInt(st), n, n + C };
                }
            }
            Arrays.sort(E, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[0] - o2[0];
                }
            });
            int ans = 0;
            int aRoot, bRoot;
            for (int[] e : E) {
                aRoot = findRoot(e[1], root);
                bRoot = findRoot(e[2], root);
                if (aRoot != bRoot) {
                    ans += e[0];
                    root[Math.max(aRoot, bRoot)] = Math.min(aRoot, bRoot);
                }
            }
            sb.append(ans).append("\n");
        }
        System.out.println(sb);
    }

    static int findRoot(int node, int[] root) {
        if (root[node] != node)
            root[node] = findRoot(root[node], root);
        return root[node];
    }

}