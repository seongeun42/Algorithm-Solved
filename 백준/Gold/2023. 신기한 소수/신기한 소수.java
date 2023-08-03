import java.io.*;
import java.util.*;

public class Main {
	
	static Set<Integer> sosu = new HashSet<>(Arrays.asList(2, 3, 5, 7));
	static StringBuilder sb = new StringBuilder();
	static int n;
	
	public static boolean isPrime(int num) {
		if (sosu.contains(num))
			return true;
		for (int i = 2; i < Math.sqrt(num) + 1; i++) {
			if (num % i == 0)
				return false;
		}
		sosu.add(num);
		return true;
	}
	
	public static void dfs(int dep, int num) {
		if (dep == n) {
			sb.append(num).append("\n");
			return;
		}
		for (int i = 0; i < 10; i++) {
			int tmp = num * 10 + i;
			if (isPrime(tmp))
				dfs(dep + 1, tmp);
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		for (int i = 2; i <= 7; i++)
			if (sosu.contains(i))
				dfs(1, i);
		System.out.println(sb);
	}
	
}