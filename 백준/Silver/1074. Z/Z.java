import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());		
		int ans = 0;
		int sr = 0, sc = 0, len = (int) Math.pow(2, N - 1);
		while (N-- > 0) {
			int cnt = (int) Math.pow(2, 2 * N);
			if (sr <= r && r < sr + len && sc + len <= c && c < sc + 2 * len) { // 2칸
				ans += cnt;
				sc += len;
			} else if (sr + len <= r && r < sr + 2 * len && sc <= c && c < sc + len) { // 3칸
				ans += cnt * 2;
				sr += len;
			} else if (sr + len <= r && r < sr + 2 * len && sc + len <= c && c < sc + 2 * len) { // 4칸
				ans += cnt * 3;
				sr += len;
				sc += len;
			}
			len /= 2;
		}
		System.out.println(ans);
	}

}