import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int W = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());
        int[][] map = new int[H][W];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(bfs(H, W, K, map));
    }

    private static int bfs(int H, int W, int K, int[][] map) {
        if (H == 1 && W == 1)
            return 0;
        int[] dx = { 0, 0, 1, -1, 1, 1, -1, -1, 2, 2, -2, -2 };
        int[] dy = { 1, -1, 0, 0, -2, 2, -2, 2, 1, -1, 1, -1 };
        int[][][] visited = new int[H][W][K + 1];
        Deque<Point> q = new ArrayDeque<>();
        visited[0][0][0] = 1;
        q.add(new Point(0, 0, K));
        while (!q.isEmpty()) {
            Point cur = q.pollFirst();
            for (int i = 0; i < 12; i++) {
                if (cur.cnt == 0 && i >= 4)
                    break;
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                int ncnt = cur.cnt;
                if (i >= 4)
                    ncnt--;
                if (0 <= nx && nx < W && 0 <= ny && ny < H && visited[ny][nx][ncnt] == 0 && map[ny][nx] == 0) {
                    if (nx == W - 1 && ny == H - 1)
                        return visited[cur.y][cur.x][cur.cnt] + 1;
                    visited[ny][nx][ncnt] = visited[cur.y][cur.x][cur.cnt] + 1;
                    q.add(new Point(nx, ny, ncnt));
                }
            }
        }
        return -1;
    }

    static class Point {
        int x, y, cnt;

        public Point(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

}