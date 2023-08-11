import java.io.*;
import java.util.*;

public class Main {
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        List<Integer[]> home = new ArrayList<>();
        List<Integer[]> chik = new ArrayList<>();
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1)
                    home.add(new Integer[]{i, j});
                else if (map[i][j] == 2)
                    chik.add(new Integer[]{i, j});
            }
        }

        int[] open = new int[chik.size()];
        for (int i = chik.size() - 1; i >= chik.size() - m; i--) {
            open[i] = 1;
        }

        do {
            int total = 0;
            for (Integer[] h : home) {
                int min_v = Integer.MAX_VALUE;
                for (int i = 0; i < chik.size(); i++) {
                    if (open[i] == 1) {
                        Integer[] c = chik.get(i);
                        min_v = Math.min(min_v, Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1]));
                    }
                }
                total += min_v;
                if (res <= total)
                    break;
            }
            res = Math.min(res, total);
        } while (np(open));
        System.out.println(res);
    }

    static boolean np(int[] mask) {
        int N = mask.length;
        int i = N - 1;
        while (i > 0 && mask[i - 1] >= mask[i]) i--;

        if (i == 0) return false;

        int j = N - 1;
        while (mask[i - 1] >= mask[j]) j--;

        int temp = mask[i - 1];
        mask[i - 1] = mask[j];
        mask[j] = temp;

        Arrays.sort(mask, i, mask.length);

        return true;
    }

}