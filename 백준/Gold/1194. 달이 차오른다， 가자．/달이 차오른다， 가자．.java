import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[] dx = { 1, -1, 0, 0 };
    static int[] dy = { 0, 0, 1, -1 };
    static int[][] miro;
    static int[][][] visited;
    static Move start;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        miro = new int[n][m];
        visited = new int[n][m][64];
        for (int i = 0; i < n; i++) {
            char[] l = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                miro[i][j] = l[j] - '0';
                if (miro[i][j] == 0) {
                    start = new Move(j, i, 0);
                }
            }
        }
        System.out.println(bfs());
    }

    static int bfs() {
        Deque<Move> q = new ArrayDeque<>();
        q.add(start);
        visited[start.y][start.x][0] = 1;
        while (!q.isEmpty()) {
            Move cur = q.pollFirst();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && visited[ny][nx][cur.keys] == 0 && miro[ny][nx] != '#' - '0') {
                    if (miro[ny][nx] == 1)
                        return visited[cur.y][cur.x][cur.keys];
                    if ('a' - '0' <= miro[ny][nx] && miro[ny][nx] <= 'f' - '0') {
                        int newKey = cur.keys | (1 << miro[ny][nx] + '0' - 'a');
                        visited[ny][nx][newKey] = visited[cur.y][cur.x][cur.keys] + 1;
                        q.add(new Move(nx, ny, newKey));
                    } else {
                        if ('A' - '0' <= miro[ny][nx] && miro[ny][nx] <= 'F' - '0' && (cur.keys & (1 << miro[ny][nx] + '0' - 'a')) == 0)
                            continue;
                        visited[ny][nx][cur.keys] = visited[cur.y][cur.x][cur.keys] + 1;
                        q.add(new Move(nx, ny, cur.keys));
                    }
                }
            }
        }
        return -1;
    }

    static class Move {
        int x, y;
        int keys;

        public Move(int x, int y, int keys) {
            this.x = x;
            this.y = y;
            this.keys = keys;
        }
    }
}