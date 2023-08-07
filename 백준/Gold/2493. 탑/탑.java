import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		Stack<int[]> s = new Stack<>();
		for (int i = 0; i < N; i++) {
			int v = Integer.parseInt(st.nextToken());
			while (!s.isEmpty() && s.peek()[0] <= v)
				s.pop();
			sb.append(!s.isEmpty() ? s.peek()[1] : 0).append(" ");
			s.add(new int[] { v , i + 1 });
		}
		System.out.println(sb);
	}
	
}
