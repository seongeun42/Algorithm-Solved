import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		int[][] src = new int[N][M], desc = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				src[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int cnt = Math.min(N, M) / 2;
		for (int i = 0; i < cnt; i++) {
			rotate(desc, src, i, N - i, i, M - i, R);
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				sb.append(desc[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
	
	static void rotate(int[][] desc, int[][] src, int sr, int er, int sc, int ec, int R) {
		int hcnt = (er - sr) * 2 + (ec - sc) * 2 - 4;
		R %= hcnt;
		
		Deque<Integer> dq = new ArrayDeque<>();
		for (int i = sc; i < ec; i++)
			dq.offerLast(src[sr][i]);
		for (int i = sr + 1; i < er; i++)
			dq.offerLast(src[i][ec - 1]);
		for (int i = ec - 2; i >= sc; i--)
			dq.offerLast(src[er - 1][i]);
		for (int i = er - 2; i > sr; i--)
			dq.offerLast(src[i][sc]);
		
		if (R <= hcnt - R)
			for (int i = 0; i < R; i++)
				dq.offerLast(dq.pollFirst());
		else
			for (int i = 0; i < hcnt - R; i++)
				dq.offerFirst(dq.pollLast());

		for (int i = sc; i < ec; i++)
			desc[sr][i] = dq.pollFirst();
		for (int i = sr + 1; i < er; i++)
			desc[i][ec - 1] = dq.pollFirst();
		for (int i = ec - 2; i >= sc; i--)
			desc[er - 1][i] = dq.pollFirst();
		for (int i = er - 2; i > sr; i--)
			desc[i][sc] = dq.pollFirst();
	}
	
}