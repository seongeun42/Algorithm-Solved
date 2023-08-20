import java.io.*;
import java.util.*;

public class Main {

    static int readInt(StringTokenizer st) { return Integer.parseInt(st.nextToken()); }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            PriorityQueue<Edge> E = new PriorityQueue<>();
            st = new StringTokenizer(br.readLine());
            int R = readInt(st), C = readInt(st);
            int[] root = new int[R * C];
            for (int i = 0; i < R * C; i++) {
                root[i] = i;
            }
            int cnt = 0;
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C - 1; j++) {
                    int n = i * C + j;
                    E.add(new Edge(readInt(st), n, n + 1));
                }
            }
            for (int i = 0; i < R - 1; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < C; j++) {
                    int n = i * C + j;
                    E.add(new Edge(readInt(st), n, n + C));
                }
            }
            int all = 0, ans = 0;
            int aRoot, bRoot;
            while (!E.isEmpty() && all < R * C - 1) {
                Edge e = E.poll();
                aRoot = findRoot(e.a, root);
                bRoot = findRoot(e.b, root);
                if (aRoot != bRoot) {
                    all++;
                    ans += e.w;
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

    static class Edge implements Comparable<Edge> {
        int w, a, b;

        public Edge(int w, int a, int b) {
            this.w = w;
            this.a = a;
            this.b = b;
        }

        @Override
        public int compareTo(Edge o) {
            return w - o.w;
        }
    }

}