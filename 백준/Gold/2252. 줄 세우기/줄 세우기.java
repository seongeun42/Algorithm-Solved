import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int N = readInt(st), M = readInt(st);
        List<List<Integer>> G = new ArrayList<>();
        int[] degree = new int[N + 1];
        for (int i = 0; i < N + 1; i++)
            G.add(new ArrayList<>());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = readInt(st), b = readInt(st);
            G.get(a).add(b);
            degree[b]++;
        }
        topology(N, degree, G, sb);
        System.out.println(sb);
    }


    static void topology(int N, int[] degree, List<List<Integer>> G, StringBuilder sb) {
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i < N + 1; i++) {
            if (degree[i] == 0)
                q.add(i);
        }
        while (!q.isEmpty()) {
            int cur = q.pollFirst();
            sb.append(cur).append(" ");
            for (int nn : G.get(cur)) {
                degree[nn]--;
                if (degree[nn] == 0)
                    q.add(nn);
            }
        }
    }

    static int readInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

}