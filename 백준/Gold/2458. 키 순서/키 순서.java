import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = readInt(st);
		int M = readInt(st);
		int[][] edges = new int[N + 1][N + 1];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			edges[readInt(st)][readInt(st)] = 1;
		}

		for (int m = 1; m <= N; m++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (edges[i][m] == 1 && edges[m][j] == 1) {
						edges[i][j] = 1;
					}
				}
			}
		}

		int ans = 0;
		for (int i = 1; i <= N; i++) {
			int know = 0;
			for (int j = 1; j <= N; j++)
				know += edges[i][j] + edges[j][i];
			if (know == N - 1)
				ans++;
		}
		
		System.out.println(ans);
	}

	static int readInt(StringTokenizer st) {
		return Integer.parseInt(st.nextToken());
	}
	
}