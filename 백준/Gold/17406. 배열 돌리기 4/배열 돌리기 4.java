import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++)
                arr[i][j] = Integer.parseInt(st.nextToken());
        }

        int[][] rot = new int[R][3];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++)
                rot[i][j] = Integer.parseInt(st.nextToken());
        }

        int[] npArr = new int[R];
        for (int i = 0; i < R; i++)
            npArr[i] = i;

        int ans = Integer.MAX_VALUE;
        do {
            int[][] resArr = copy(arr);
            for (int i = 0; i < R; i++) {
                int r = rot[npArr[i]][0], c = rot[npArr[i]][1], s = rot[npArr[i]][2];
                rotate(resArr, copy(resArr), r - s - 1, r + s, c - s - 1, c + s, s);
            }

            for (int i = 0; i < N; i++) {
                int sum = 0;
                for (int j = 0; j < M; j++) {
                    sum += resArr[i][j];
                }
                if (sum < ans)
                    ans = sum;
            }
        } while (nextPermutation(npArr));

        System.out.println(ans);
    }

    static boolean nextPermutation(int[] pre) {
        int N = pre.length;
        int i = N - 1;
        while (i > 0 && pre[i - 1] >= pre[i]) i--;

        if (i == 0) return false;

        int j = N - 1;
        while (pre[i - 1] >= pre[j]) j--;

        swap(pre, i - 1, j);

        int k = N - 1;
        while (i < k) {
            swap(pre, i++, k--);
        }

        return true;
    }

    static void swap(int[] p, int a, int b) {
        int temp = p[a];
        p[a] = p[b];
        p[b] = temp;
    }

    static int[][] copy(int[][] src) {
        int[][] desc = new int[src.length][];
        for (int i = 0; i < src.length; i++) {
            desc[i] = Arrays.copyOf(src[i], src[i].length);
        }
        return desc;
    }

    static void rotate(int[][] desc, int[][] src, int sr, int er, int sc, int ec, int cnt) {
        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };

        for (int i = 0; i < cnt; i++) {
            int total = (((cnt - i) * 2) + 1) * 4 - 5;
            desc[sr + i][sc + i + 1] = src[sr + i][sc + i];
            int nr = sr + i, nc = sc + i;
            int d = 0;
            while (total > 0) {
                if (sr + i > nr + dy[d] || nr + dy[d] >= er - i || sc + i > nc + dx[d] || nc + dx[d] >= ec - i) {
                    d = (d + 1) % 4;
                    continue;
                }
                desc[nr][nc] = src[nr + dy[d]][nc + dx[d]];
                nr += dy[d];
                nc += dx[d];
                total--;
            }
        }
    }

}