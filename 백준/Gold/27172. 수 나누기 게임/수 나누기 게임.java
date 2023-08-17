import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] X = new int[N];
        boolean[] exist = new boolean[1000001];
        int maxX = 0;
        for (int i = 0; i < N; i++) {
            X[i] = Integer.parseInt(st.nextToken());
            exist[X[i]] = true;
            if (maxX < X[i])
                maxX = X[i];
        }
        int[] score = new int[maxX + 1];
        for (int x : X) {
            for (int i = x + x; i <= maxX; i += x) {
                if (exist[i]) {
                    score[i]--;
                    score[x]++;
                }
            }
        }
        for (int x : X)
            sb.append(score[x]).append(" ");
        System.out.println(sb);
    }

}