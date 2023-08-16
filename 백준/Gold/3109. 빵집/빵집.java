import java.io.*;
import java.util.*;

public class Main {
	
	static int[] dy = { -1, 0, 1 };
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());		
		String[] map = new String[R];
		for (int i = 0; i < R; i++)
			map[i] = br.readLine();
		boolean[][] visit = new boolean[R][C];
		int res = 0;
		for (int i = 0; i < R; i++)
			if (connect(map, visit, i, 0, C)) res++;
		System.out.println(res);
	}
	
	static boolean connect(String[] map, boolean[][] visit, int cr, int cc, int C) {
		visit[cr][cc] = true;
		if (cc == C - 1) {
			return true;
		}
		for (int i = 0; i < 3; i++) {
			int nr = cr + dy[i], nc = cc + 1;
			if (0 <= nr && nr < map.length && 0 <= nc && nc < C && !visit[nr][nc] && map[nr].charAt(nc) == '.') {
				if (connect(map, visit, nr, nc, C))
					return true;
			}
		}
		return false;
	}
	
}