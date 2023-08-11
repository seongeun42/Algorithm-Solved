import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] h = new int[N];
        for (int i = 0; i < N; i++)
            h[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(h);
        for (int i = 0; i < N; i++) {
            if (h[i] > L) break;
            L++;
        }
        System.out.println(L);
    }

}