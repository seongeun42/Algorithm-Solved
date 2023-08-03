import java.io.*;
import java.util.*;

public class Main {
	
	static int n, ans = 1000000000;
	static int[][] taste;
	
	public static void dfs(int dep, int s, int b) {
		if (dep == n) {
			if (s != 0 && ans > Math.abs(s - b)) {
				ans = Math.abs(s - b);
			}
			return;
		}
		
		int sv = taste[dep][0], bv = taste[dep][1];
		dfs(dep + 1, s == 0 ? sv : s * sv, b + bv);
		dfs(dep + 1, s, b);
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		taste = new int[n][2];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			taste[i][0] = Integer.parseInt(st.nextToken());
			taste[i][1] = Integer.parseInt(st.nextToken());			
		}
		dfs(0, 0, 0);
		System.out.println(ans);
	}
	
}