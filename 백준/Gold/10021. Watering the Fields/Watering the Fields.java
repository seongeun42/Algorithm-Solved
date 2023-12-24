import java.io.*;
import java.util.*;

public class Main {

    static int[] R;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
        Field[] fields = new Field[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            fields[i] = new Field(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cost = (int) (Math.pow(fields[i].x - fields[j].x, 2) + Math.pow(fields[i].y - fields[j].y, 2));
                if (cost >= c) {
                    edges.add(new Edge(cost, i, j));
                }
            }
        }
        edges.sort(new Comparator<Edge>() {
            @Override
            public int compare(Edge o1, Edge o2) {
                return o1.cost - o2.cost;
            }
        });

        R = new int[n];
        for (int i = 0; i < n; i++)
            R[i] = i;
        int ans = 0;
        int cnt = 1;
        for (Edge e : edges) {
            if (cnt == n)
                break;
            int ir = findRoot(e.i);
            int jr = findRoot(e.j);
            if (ir != jr) {
                ans += e.cost;
                cnt++;
                R[Math.max(ir, jr)] = Math.min(ir, jr);
            }
        }

        System.out.println(cnt == n ? ans : -1);
    }

    static int findRoot(int n) {
        if (R[n] != n)
            R[n] = findRoot(R[n]);
        return R[n];
    }

    static class Field {
        int x, y;

        public Field(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static class Edge {
        int cost, i, j;

        public Edge(int cost, int i, int j) {
            this.cost = cost;
            this.i = i;
            this.j = j;
        }
    }

}