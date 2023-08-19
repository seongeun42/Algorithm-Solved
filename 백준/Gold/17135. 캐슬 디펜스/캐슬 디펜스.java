import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = readInt(st), M = readInt(st), D = readInt(st);
        String[][] pan = new String[N][M];
        for (int i = 0; i < N; i++) {
            pan[i] = br.readLine().split(" ");
        }

        int idx = 0;
        int[] mask = new int[M];
        while (idx++ < 3)
            mask[M - idx] = 1;

        int ans = 0;
        do {
            int[] arch = new int[3];
            idx = 0;
            for (int i = 0; i < M; i++) {
                if (mask[i] == 1)
                    arch[idx++] = i;
            }

            int[] dx = { -1, 0, 1 };
            int[] dy = { 0, -1, 0 };

            String[][] map = new String[N][M];
            for (int i = 0; i < N; i++) {
                map[i] = pan[i].clone();
            }

            int kill = 0;
            boolean[][] killCheck = new boolean[N][M];
            for (int r = N; r > 0; r--) {
                boolean[] archKill = new boolean[3];
                Deque<int[]> q = new ArrayDeque<>();
                Deque<int[]> dead = new ArrayDeque<>();
                for (int a = 0; a < 3; a++) {
                    q.addLast(new int[] { r - 1, arch[a], 1, a });
                }
                while (!q.isEmpty() && dead.size() < 3) {
                    int[] cur = q.pollFirst();
                    if (archKill[cur[3]]) continue;
                    if (map[cur[0]][cur[1]].equals("1")) {
                        if (!killCheck[cur[0]][cur[1]]) {
                            dead.addLast(new int[] { cur[0], cur[1] });
                            killCheck[cur[0]][cur[1]] = true;
                        }
                        archKill[cur[3]] = true;
                        continue;
                    }
                    for (int d = 0; d < 3; d++) {
                        int ny = cur[0] + dy[d];
                        int nx = cur[1] + dx[d];
                        if (0 <= nx && nx < M && 0 <= ny && ny < N && cur[2] < D) {
                            q.add(new int[] { ny, nx, cur[2] + 1, cur[3] });
                        }
                    }
                }
                kill += dead.size();
                for (int[] yx : dead) {
                    map[yx[0]][yx[1]] = "0";
                }
            }
            if (kill > ans)
                ans = kill;
        } while (np(mask));
        System.out.println(ans);
    }

    static boolean np(int[] p) {
        int N = p.length;
        int i = N - 1;
        while (i > 0 && p[i - 1] >= p[i]) i--;

        if (i == 0) return false;

        int j = N - 1;
        while (p[i - 1] >= p[j]) j--;

        int temp = p[i - 1];
        p[i - 1] = p[j];
        p[j] = temp;

        Arrays.sort(p, i, p.length);
        return true;
    }

    static int readInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

}