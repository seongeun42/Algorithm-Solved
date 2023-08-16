import java.io.*;
import java.util.*;

public class Main {

    static int[][] GAME = new int[6][3];
    static int[] A = new int[15];
    static int[] B = new int[15];

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int idx = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = i + 1; j < 6; j++) {
                A[idx] = i;
                B[idx++] = j;
            }
        }

        for (int tc = 0; tc < 4; tc++) {
            int all = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    GAME[i][j] = Integer.parseInt(st.nextToken());
                    all += GAME[i][j];
                }
            }

            if (all > 30) {
                sb.append("0 ");
                continue;
            }

            if (!backtrack(0))
                sb.append("0 ");
        }
        System.out.println(sb);
    }

    static boolean backtrack(int dep) {
        if (dep == 15) {
            sb.append("1 ");
            return true;
        }
        
        if (GAME[A[dep]][0] > 0 && GAME[B[dep]][2] > 0) {
            GAME[A[dep]][0]--;
            GAME[B[dep]][2]--;
            if (backtrack(dep + 1))
                return true;
            GAME[A[dep]][0]++;
            GAME[B[dep]][2]++;
        }

        if (GAME[A[dep]][1] > 0 && GAME[B[dep]][1] > 0) {
            GAME[A[dep]][1]--;
            GAME[B[dep]][1]--;
            if (backtrack(dep + 1))
                return true;
            GAME[A[dep]][1]++;
            GAME[B[dep]][1]++;
        }
        
        if (GAME[A[dep]][2] > 0 && GAME[B[dep]][0] > 0) {
            GAME[A[dep]][2]--;
            GAME[B[dep]][0]--;
            if (backtrack(dep + 1))
                return true;
            GAME[A[dep]][2]++;
            GAME[B[dep]][0]++;
        }

        return false;
    }

}