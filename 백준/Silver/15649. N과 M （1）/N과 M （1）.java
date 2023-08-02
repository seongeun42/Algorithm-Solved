import java.io.*;
import java.util.*;

public class Main {
	
    static int n, m;
	static int[] check;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		check = new int[n];
		permutation(0, "");
		System.out.println(sb.toString());
	}
	
	public static void permutation(int dep, String s) {
		if (dep == m) {
			sb.append(s.trim()).append("\n");
			return;
		}
		for (int i = 1; i <= n; i++) {
			if (check[i - 1] == 0) {
				check[i - 1] = 1;
				permutation(dep + 1, s + " " + i);
				check[i - 1] = 0;
			}
		}
	}
}