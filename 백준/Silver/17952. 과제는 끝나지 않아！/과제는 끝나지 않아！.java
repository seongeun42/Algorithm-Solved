import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		Deque<int[]> task = new ArrayDeque<>();
		int time = 0;
		int a = 0, t = 0;
		int score = 0;
		while (time++ < N) {
			st = new StringTokenizer(br.readLine());
			if (st.nextToken().equals("1")) {
				if (a != 0) {
					task.addLast(new int[] { a, t });
				}
				a = Integer.parseInt(st.nextToken());
				t = Integer.parseInt(st.nextToken());
			}
			t--;
			if (t == 0) {
				score += a;
				if (!task.isEmpty()) {
					int[] old = task.pollLast();
					a = old[0];
					t = old[1];
				}
			}
		}
		System.out.println(score);
	}

}