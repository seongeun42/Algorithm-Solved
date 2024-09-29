import java.io.*;
import java.util.*;

public class Main {
	
	static List<List<Integer>> graph = new ArrayList<>();
	static StringBuilder sb = new StringBuilder();
	static boolean[] visited;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = readInt(st), M = readInt(st), V = readInt(st);
		visited = new boolean[N + 1];
		for (int i = 0; i <= N; i++) {
			graph.add(new ArrayList<>());
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = readInt(st), b = readInt(st);
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		for (int i = 1; i <= N; i++) {
			Collections.sort(graph.get(i));
		}
		
		dfs(V);
		sb.append("\n");
		bfs(V);
		System.out.println(sb);
	}
	
	static int readInt(StringTokenizer st) {
		return Integer.parseInt(st.nextToken());
	}
	
	static void dfs(int node) {
		visited[node] = true;
		sb.append(node).append(" ");
		for (Integer v : graph.get(node)) {
			if (!visited[v])
				dfs(v);
		}
	}
	
	static void bfs(int start) {
		Deque<Integer> q = new ArrayDeque<>();
		q.add(start);
		visited[start] = false;
		while (!q.isEmpty()) {
			int node = q.pollFirst();
			sb.append(node).append(" ");
			for (Integer v : graph.get(node)) {
				if (visited[v]) {
					q.add(v);
					visited[v] = false;
				}
			}
		}
	}

}