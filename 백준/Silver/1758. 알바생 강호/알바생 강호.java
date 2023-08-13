import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] tips = new Integer[N];
        for (int i = 0; i < N; i++) {
            tips[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(tips, Comparator.reverseOrder());
        long ans = 0L;
        for (int i = 0; i < N; i++) {
            if (tips[i] - i <= 0) break;
            ans += tips[i] - i;
        }
        System.out.println(ans);
    }

}