import java.io.*;
import java.util.*;

class Main {

    static int R, C;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] forest;
    static Point hed, bea;
    static Deque<Point> water = new ArrayDeque<>();
    static int X = Integer.MAX_VALUE, dot = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        forest = new int[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                if (line.charAt(j) == '.') {
                    forest[i][j] = dot;
                } else if (line.charAt(j) == '*') {
                    forest[i][j] = 0;
                    water.add(new Point(j, i));
                } else if (line.charAt(j) == 'S') {
                    forest[i][j] = 0;
                    hed = new Point(j, i);
                } else if (line.charAt(j) == 'D') {
                    forest[i][j] = 2500;
                    bea = new Point(j, i);
                } else if (line.charAt(j) == 'X') {
                    forest[i][j] = X;
                }
            }
        }
        flood();
        System.out.println(bfs());
    }

    static String bfs() {
        Deque<Point> q = new ArrayDeque<>();
        q.offer(hed);
        while (!q.isEmpty()) {
            Point cur = q.pollFirst();
            if (cur.x == bea.x && cur.y == bea.y) {
                return String.valueOf(forest[cur.y][cur.x]);
            }
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (0 <= nx && nx < C && 0 <= ny && ny < R) {
                    if (forest[ny][nx] != X && forest[ny][nx] != dot) {
                        if (forest[cur.y][cur.x] + 1 < Math.abs(forest[ny][nx])) {
                            forest[ny][nx] = forest[cur.y][cur.x] + 1;
                            q.offer(new Point(nx, ny));
                        }
                    } else if (forest[ny][nx] == dot) {
                        forest[ny][nx] = forest[cur.y][cur.x] + 1;
                        q.offer(new Point(nx, ny));
                    }
                }
            }
        }
        return "KAKTUS";
    }

    static void flood() {
        while (!water.isEmpty()) {
            Point cur = water.pollFirst();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (0 <= nx && nx < C && 0 <= ny && ny < R) {
                    if (forest[ny][nx] == dot) {
                        forest[ny][nx] = forest[cur.y][cur.x] - 1;
                        water.add(new Point(nx, ny));
                    }
                }
            }
        }
    }

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

}