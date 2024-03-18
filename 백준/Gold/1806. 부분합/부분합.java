import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		int[] nums = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int ans = N + 1, sum = nums[0];
		int s = 0, e = 0;
		while (s <= e) {
			if (ans == 1)
				break;
			if (sum < S) {
				if (e == N - 1)
					break;
				e++;
				sum += nums[e];
			} else {
				if (ans > e - s + 1)
					ans = e - s + 1;
				sum -= nums[s];
				s++;
			}
		}
		System.out.println(ans != N + 1 ? ans : 0);
	}
	
}