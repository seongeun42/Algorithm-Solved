import java.io.*;
import java.util.*;

public class Main {

  static int N, M, empty, ans = 2500;
  static int[][] lab;
  static List<Point> virus = new ArrayList<>();

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = readInt(st);
    M = readInt(st);
    lab = new int[N][N];
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      for (int j = 0; j < N; j++) {
        int v = readInt(st);
        lab[i][j] = v;
        if (v == 1) continue;
        if (v == 2) {
          virus.add(new Point(i, j));
        }
        ++empty;
      }
    }
    combination(-1, 0, new ArrayList<>());
    System.out.println(ans != 2500 ? ans : -1);
  }

  static int bfs(List<Point> arr, int remain) {
    int[] dy = {1, 0, -1, 0};
    int[] dx = {0, 1, 0, -1};
    Deque<Point> q = new ArrayDeque<>();
    remain -= M;
    if (remain == 0) {
      return 0;
    }
    int[][] visited = new int[N][N];
    for (Point p : arr) {
      q.add(p);
      visited[p.y][p.x] = 1;
    }
    int time = 0;
    while (!q.isEmpty()) {
      Point cur = q.pollFirst();
      for (int d = 0; d < 4; d++) {
        int ny = cur.y + dy[d], nx = cur.x + dx[d];
        if (0 <= ny && ny < N && 0 <= nx && nx < N && visited[ny][nx] == 0 && lab[ny][nx] != 1) {
          visited[ny][nx] = visited[cur.y][cur.x] + 1;
          --remain;
          if (visited[ny][nx] > time) {
            time = visited[ny][nx];
          }
          q.add(new Point(ny, nx));
        }
      }
    }
    return remain == 0 ? time - 1 : -1;
  }

  static void combination(int cur, int dep, List<Point> arr) {
    if (dep == M) {
      int time = bfs(arr, empty);
      if (time != -1 && time < ans) {
        ans = time;
      }
      return;
    }
    for (int i = cur + 1; i < virus.size(); i++) {
      arr.add(virus.get(i));
      combination(i, dep + 1, arr);
      arr.remove(dep);
    }
  }

  static int readInt(StringTokenizer st) {
    return Integer.parseInt(st.nextToken());
  }

  static class Point {
    int y, x;

    Point(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

}