import java.io.*;
import java.util.*;

public class Main {

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[][] picIll = new char[N][N];
        char[][] pic = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                char c = line.charAt(j);
                pic[i][j] = c;
                picIll[i][j] = c == 'G' ? 'R' : c;
            }
        }

        int ans = 0, ansIll = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (pic[i][j] != ' ')
                    ans += dfs(i, j, pic);
                if (picIll[i][j] != ' ')
                    ansIll += dfs(i, j, picIll);
            }
        }
        System.out.printf("%d %d", ans, ansIll);
    }

    static int dfs(int y, int x, char[][] map) {
        char c = map[y][x];
        map[y][x] = ' ';
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i], nx = x + dx[i];
            if (0 <= nx && nx < map.length && 0 <= ny && ny < map.length) {
                if (map[ny][nx] == c)
                    dfs(ny, nx, map);
            }
        }
        return 1;
    }

}