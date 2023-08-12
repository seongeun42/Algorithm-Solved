import java.io.*;
import java.util.*;

public class Main {

    static int readInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        Deque<int[]> q = new ArrayDeque<>();
        PriorityQueue<int[]> not = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });
        int N = readInt(st), T = readInt(st), W = readInt(st);
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            q.addLast(new int[] { readInt(st), readInt(st), 0 });
        }

        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            not.offer(new int[] { readInt(st), readInt(st), readInt(st) });
        }

        int t = 0;
        while (t < W) {
            int[] cur = q.poll();
            for (int i = 0; i < T && cur[1] > 0 && t++ < W; i++) {
                cur[1]--;
                sb.append(cur[0]).append("\n");
                if (!not.isEmpty() && t == not.peek()[2]) {
                    q.addLast(not.poll());
                }
            }
            if (cur[1] > 0) {
                cur[2] += T;
                q.addLast(cur);
            }
        }

        System.out.println(sb);
    }

}