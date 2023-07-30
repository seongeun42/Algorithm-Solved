import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        char[] ans = new char[N];
        Arrays.fill(ans, '?');
        for (int i = 0; i < H; i++) {
            String s = br.readLine();
            for (int j = 0; j < N * W; j++) {
                if (s.charAt(j) != '?') {
                    ans[j / W] = s.charAt(j);
                }
            }
        }
        System.out.println(new String(ans));
    }
}