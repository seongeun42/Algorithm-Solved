import java.io.*;
import java.util.*;

public class Main {
	
	static int[][] map;
	static int n, m, land;
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {-1, 0, 1, 0};
	static boolean[][] visited;
	static List<Edge> edges = new ArrayList<>();
	static int[] R;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		visited = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 1)
					dfs(j, i, ++land + 1);
			}
		}
		R = new int[land + 1];
		Arrays.fill(R, -1);
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0 && !visited[i][j]) {
					bfs(j, i);
				}
			}
		}
		
		Collections.sort(edges);
		int cnt = 1;
		int dist = 0;
		for (Edge edge : edges) {
			int aroot = findRoot(edge.a);
			int broot = findRoot(edge.b);
			if (aroot != broot) {
				dist += edge.dist;
				if (R[aroot] < R[broot]) {
					R[aroot] += R[broot];
					R[broot] = aroot;
				} else {
					R[broot] += R[aroot];
					R[aroot] = broot;
				}
				cnt++;
			}
			if (cnt == land)
				break;
		}
		System.out.println(cnt == land ? dist : -1);
	}
	
	static int findRoot(int node) {
		if (R[node] < 0)
			return node;
		else
			R[node] = findRoot(R[node]);
		return R[node];
	}
	
	static void dfs(int cx, int cy, int num) {
		map[cy][cx] = num;
		for (int i = 0; i < 4; i++) {
			int nx = cx + dx[i], ny = cy + dy[i];
			if (0 <= nx && nx < m && 0 <= ny && ny < n && map[ny][nx] == 1)
				dfs(nx, ny, num);
		}
	}
	
	static void bfs(int sx, int sy) {
		Deque<Point> q = new ArrayDeque<>();
		q.add(new Point(sx, sy));
		visited[sy][sx] = true;
		while (!q.isEmpty()) {
			Point cur = q.pollFirst();
			for (int i = 0; i < 4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];
				if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[ny][nx]) {
					visited[ny][nx] = true;
					if (map[ny][nx] == 0) {
						q.add(new Point(nx, ny));
					} else {
						for (int j = 0; j < 4; j++) {
							int nnx = nx + dx[j];
							int nny = ny + dy[j];
							int dist = 0;
							while (0 <= nnx && nnx < m && 0 <= nny && nny < n && map[nny][nnx] == 0) {
								nnx += dx[j];
								nny += dy[j];
								dist++;
							}
							if (0 <= nnx && nnx < m && 0 <= nny && nny < n && dist > 1) {
								if (map[nny][nnx] != 0 && map[nny][nnx] != map[ny][nx]) {
									edges.add(new Edge(map[ny][nx] - 1, map[nny][nnx] - 1, dist));
								}
							}
						}
					}
				}
			}
		}
	}
	
	static class Edge implements Comparable<Edge> {
		int a, b, dist;

		public Edge(int a, int b, int dist) {
			this.a = a;
			this.b = b;
			this.dist = dist;
		}

		@Override
		public int compareTo(Edge o) {
			return dist - o.dist;
		}
	}
	
	static class Point {
		int x, y;
		
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
}