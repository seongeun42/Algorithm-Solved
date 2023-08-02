import java.io.*;
import java.util.*;

public class Main {
	
	static int N, M;
    static int[] check;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		check = new int[N];
		combination(0, 0, "");
		System.out.println(sb);
	}
	
	public static void combination(int pre, int dep, String s) {
		if (dep == M) {
			sb.append(s.trim() + "\n");
			return;
		}
		for (int i = pre + 1; i <= N; i++) {
			if (check[i - 1] == 0) {
				check[i - 1] = 1;
				combination(i, dep + 1, s + " " + i);
				check[i - 1] = 0;
			}
		}
	}
	
}