import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int k = Integer.parseInt(br.readLine());
        String[] cmd = new String[2 * k];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 2 * k; i++) {
            cmd[i] = st.nextToken();
        }
        int h = Integer.parseInt(br.readLine());
        int len = (int) Math.pow(2, k);
        int[][] paper = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                paper[i][j] = -1;
            }
        }
        recur(0, cmd, paper, 0, 0, len, len, h);

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                sb.append(paper[i][j]).append(" ");
            }
            sb.append("\n");
        }
		System.out.println(sb);
    }

    static void recur(int dep, String[] cmd, int[][] paper, int sr, int sc, int ySize, int xSize, int h) {
        if (dep == cmd.length) {
            paper[sr][sc] = h;
            return;
        }

        switch (cmd[dep]) {
            case "D":
                recur(dep + 1, cmd, paper, sr + ySize / 2, sc, ySize / 2, xSize, h);
                for (int i = sr; i < sr + ySize / 2; i++) {
                    punchDU(paper, sc, xSize, sr + sr + ySize - 1, i);
                }
                break;
            case "U":
                recur(dep + 1, cmd, paper, sr, sc, ySize / 2, xSize, h);
                for (int i = sr + ySize / 2; i < sr + ySize; i++) {
                    punchDU(paper, sc, xSize, sr + sr + ySize - 1, i);
                }
                break;
            case "R":
                recur(dep + 1, cmd, paper, sr, sc + xSize / 2, ySize, xSize / 2, h);
                for (int i = sr; i < sr + ySize; i++) {
                    for (int j = sc; j < sc + xSize / 2; j++) {
                        punchRL(paper, sc + sc + xSize - 1, i, j);
                    }
                }
                break;
            case "L":
                recur(dep + 1, cmd, paper, sr, sc, ySize, xSize / 2, h);
                for (int i = sr; i < sr + ySize; i++) {
                    for (int j = sc + xSize / 2; j < sc + xSize; j++) {
                        punchRL(paper, sc + sc + xSize - 1, i, j);
                    }
                }
                break;
        }
    }

    private static void punchRL(int[][] paper, int hap, int i, int j) {
        if (paper[i][hap - j] == 0)
            paper[i][j] = 1;
        else if (paper[i][hap - j] == 1)
            paper[i][j] = 0;
        else if (paper[i][hap - j] == 2)
            paper[i][j] = 3;
        else if (paper[i][hap - j] == 3)
            paper[i][j] = 2;
    }

    private static void punchDU(int[][] paper, int sc, int xSize, int hap, int i) {
        for (int j = sc; j < sc + xSize; j++) {
            if (paper[hap - i][j] == 0)
                paper[i][j] = 2;
            else if (paper[hap - i][j] == 2)
                paper[i][j] = 0;
            else if (paper[hap - i][j] == 1)
                paper[i][j] = 3;
            else if (paper[hap - i][j] == 3)
                paper[i][j] = 1;
        }
    }

}