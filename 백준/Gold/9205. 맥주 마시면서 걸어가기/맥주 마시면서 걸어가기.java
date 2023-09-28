import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int n;
	static int[][] dist;
	static boolean[] visited;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			n = Integer.parseInt(br.readLine());
			visited = new boolean[n + 2];
			dist = new int[n + 2][2];
			for (int i = 0; i < n + 2; i++) {
				st = new StringTokenizer(br.readLine());
				dist[i][0] = Integer.parseInt(st.nextToken());
				dist[i][1] = Integer.parseInt(st.nextToken());				
			}
			dfs(0);
			sb.append(visited[n + 1] ? "happy\n" : "sad\n");
		}
		System.out.println(sb);
	}
	
	static void dfs(int node) {
		visited[node] = true;
		for (int i = 0; i < n + 2; i++) {
			if (!visited[i] && Math.abs(dist[node][0] - dist[i][0]) + Math.abs(dist[node][1] - dist[i][1]) <= 1000) {
				dfs(i);
			}
		}
	}

}