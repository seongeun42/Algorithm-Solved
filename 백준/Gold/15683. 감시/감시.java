import java.io.*;
import java.util.*;

public class Main {

    // 북동남서
    static int[] dc = {0, 1, 0, -1};
    static int[] dr = {-1, 0, 1, 0};
    // CCTV 방향 : 북동남서 0123
    static int[][][] mode = {
            {},
            {{0}, {1}, {2}, {3}},
            {{0, 2}, {1, 3}},
            {{0, 1}, {1, 2}, {2, 3}, {0, 3}},
            {{0, 1, 3}, {1, 2, 3}, {0, 1, 2}, {0, 2, 3}},
            {{0, 1, 2, 3}}
    };

    static int N, M, ans = 64;
    static int[][] room;
    static List<int[]> cctvs = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        room = new int[N][M];
        cctvs = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                room[i][j] = num;
                if (1 <= num && num < 6)
                    cctvs.add(new int[] {num, i, j});
            }
        }
        dfs(0, room);
        System.out.println(ans);
    }

    static void dfs(int dep, int[][] arr) {
        if (dep == cctvs.size()) {
            int zeroCnt = 0;
            for (int i = 0; i < N; i++)
                for (int j = 0; j < M; j++)
                    if (arr[i][j] == 0)
                        zeroCnt++;
            if (ans > zeroCnt)
                ans = zeroCnt;
            return;
        }
        int[][] tmp = new int[N][M];
        for (int i = 0; i < N; i++)
            tmp[i] = arr[i].clone();
        int[] cctv = cctvs.get(dep);
        for (int[] m : mode[cctv[0]]) {
            fill(tmp, m, cctv[1], cctv[2]);
            dfs(dep + 1, tmp);
            tmp = new int[N][M];
            for (int i = 0; i < N; i++)
                tmp[i] = arr[i].clone();
        }
    }

    static void fill(int[][] arr, int[] directs, int r, int c) {
        for (int d : directs) {
            int nr = r, nc = c;
            while (true) {
                nr += dr[d];
                nc += dc[d];
                if (0 > nr || nr >= N || 0 > nc || nc >= M || arr[nr][nc] == 6)
                    break;
                if (arr[nr][nc] == 0)
                    arr[nr][nc] = 7;
            }
        }
    }

}