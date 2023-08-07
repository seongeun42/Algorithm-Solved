import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder("<");
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		List<Integer> ll = new LinkedList<>();
		for (int i = 1; i <= N; i++) {
			ll.add(i);
		}
		int idx = 0;
		for (int i = 0; i < N; i++) {
			idx = (K - 1 + idx) % ll.size();
			sb.append(ll.get(idx)).append(ll.size() == 1 ? ">" : ", ");
			ll.remove(idx);
		}
		System.out.println(sb);
	}
	
}