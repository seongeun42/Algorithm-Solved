import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int V = readInt(st), E = readInt(st);
		int S = Integer.parseInt(br.readLine());
		List<Edge>[] edges = new ArrayList[V + 1];
		for (int i = 0; i <= V; i++) {
			edges[i] = new ArrayList<>();
		}
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int u = readInt(st), v = readInt(st), w = readInt(st);
			edges[u].add(new Edge(v, w));
		}
		
		int[] dp = new int[V + 1];
		Arrays.fill(dp, Integer.MAX_VALUE);
		dp[S] = 0;
		Dijkstra(S, dp, edges);
		for (int i = 1; i <= V; i++) {
			sb.append(dp[i] == Integer.MAX_VALUE ? "INF" : dp[i]).append("\n");
		}
		System.out.println(sb);
	}
	
	static void Dijkstra(int s, int[] dp, List<Edge>[] edges) {
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		pq.add(new Edge(s, 0));
		while (!pq.isEmpty()) {
			Edge cur = pq.poll();
			if (dp[cur.v] < cur.w)
				continue;
			for (Edge next : edges[cur.v]) {
				int w = next.w + cur.w;
				if (w < dp[next.v]) {
					dp[next.v] = w;
					pq.add(new Edge(next.v, w));
				}
			}
		}
	}
	
	static int readInt(StringTokenizer st) {
		return Integer.parseInt(st.nextToken());
	}
	
	static class Edge implements Comparable<Edge> {
		int v, w;

		public Edge(int v, int w) {
			this.v = v;
			this.w = w;
		}
		
		@Override
		public int compareTo(Edge o) {
			return w - o.w;
        }
	}

}